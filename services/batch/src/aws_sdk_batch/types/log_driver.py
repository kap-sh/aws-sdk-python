"""Generated from Smithy shape ``com.amazonaws.batch#LogDriver``."""

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


# --- restJson1 ser/de ---
def serialize_json(value: LogDriver) -> str:
    return value


def deserialize_json(data: str) -> LogDriver:
    return cast(LogDriver, data)
