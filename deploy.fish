#!/bin/fish
sam build -t template.yaml --config-file samconfig.toml
sam deploy -t template.yaml --config-file samconfig.toml

