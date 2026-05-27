"""Generated from Smithy shape ``com.amazonaws.ecs#LogDriver``."""

from typing import Literal, TypeAlias

LogDriver: TypeAlias = Literal[
    "json-file",
    "syslog",
    "journald",
    "gelf",
    "fluentd",
    "awslogs",
    "splunk",
    "awsfirelens",
]
