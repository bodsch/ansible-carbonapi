
ansible role to install and configure carbonapi.


[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bodsch/ansible-carbonapi/CI)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-carbonapi)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-carbonapi)][releases]

[ci]: https://github.com/bodsch/ansible-carbonapi/actions
[issues]: https://github.com/bodsch/ansible-carbonapi/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-carbonapi/releases

Ansible Role for [carbonapi](https://github.com/go-graphite/carbonapi).
> golang reimplementation of API for graphite

*carbonapi* works between *grafana* as display-layer and *go-carbon* as storage engine.

## Operating systems

Tested on

* Debian 9 / 10
* Ubuntu 18.04 / 20.04
* CentOS 8
* OracleLinux 8
* Oracle Linux 8

## Communication relationship

![schema](carbonapi.png)

## tests

```
tox -e py38-ansible29 -- molecule test
```


## install packages
https://packagecloud.io/go-graphite/stable/install#manual

## example configurations

under https://github.com/go-graphite/carbonapi/tree/0.12/cmd/carbonapi

https://github.com/go-graphite/carbonapi/blob/0.12/cmd/carbonapi/carbonapi.example.yaml
