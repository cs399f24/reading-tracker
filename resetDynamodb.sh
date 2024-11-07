#!/bin/bash

aws dynamodb delete-table --table-name bookshelf

aws dynamodb wait table-not-exists --table-name bookshelf

aws dynamodb create-table --table-name bookshelf \
    --attribute-definitions AttributeName=BookID,AttributeType=S \
    --key-schema AttributeName=BookID,KeyType=HASH \
    --provisioned-throughput ReadCapacityUnits=5,WriteCapacityUnits=5
