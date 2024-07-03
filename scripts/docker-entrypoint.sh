#!/bin/bash

params=()
if [[ "$JP_AUTHENTICATED" == false ]]; then
    params+=(--LabApp.token='')
fi
jupyter lab --ip 0.0.0.0 --port 8888 --allow-root "${params[@]}"
