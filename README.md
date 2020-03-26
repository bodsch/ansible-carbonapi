# ansible role for carbonapi

Ansible Role for [carbonapi](https://github.com/go-graphite/carbonapi).
> golang reimplementation of API for graphite

*carbonapi* works between *grafana* as display-layer and *go-carbon* as storage engine.

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
