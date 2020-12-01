import pytest
import os
import yaml
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])


@pytest.mark.parametrize("dirs", [
    "/etc/carbonapi",
    "/var/log/carbonapi"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/etc/carbonapi/carbonapi.yaml",
    "/etc/carbonapi/graphiteWeb.yaml",
    "/etc/carbonapi/graphTemplates.yaml"
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_carbonapi_service(host):
    service = host.service("carbonapi")

    if( service.__class__.__name__ != 'SysvService' ):
        assert service.is_enabled == True
    assert service.is_running == True


@pytest.mark.parametrize("ports", [
    '127.0.0.1:8088'
])
def test_open_port(host, ports):
    for i in host.socket.get_listening_sockets():
        print( i )

    socket = host.socket("tcp://{}".format(ports))
    assert socket.is_listening


def test_storage_schemas(host):

    config_file = "/etc/carbonapi/carbonapi.yaml"
    content = host.file(config_file).content_string

    assert 'listen: "localhost:8088"' in content
    assert 'host: "127.0.0.1:2003"' in content
    assert 'interval: "30s"' in content
    assert '"http://127.0.0.1:8081"' in content
