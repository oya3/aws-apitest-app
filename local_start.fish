#!/bin/fish
sam build -t template.yaml --config-file samconfig.toml
sam local start-api -t template.yaml --config-file samconfig.toml

