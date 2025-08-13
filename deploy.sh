#!/bin/bash
echo "Starting deployment..."

DEST_DIR="$HOME/python-ci-cd-deploy"
mkdir -p $DEST_DIR
cp -r app $DEST_DIR

echo "Deployment complete! Files copied to $DEST_DIR"
