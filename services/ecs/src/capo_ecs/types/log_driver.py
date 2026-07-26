"""Generated from Smithy shape ``com.amazonaws.ecs#LogDriver``."""

from typing import Literal, TypeAlias, cast

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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LogDriver) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogDriver:
    return cast(LogDriver, data)
