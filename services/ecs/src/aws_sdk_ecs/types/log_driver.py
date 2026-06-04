"""Generated from Smithy shape ``com.amazonaws.ecs#LogDriver``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_ecs.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "json-file",
        "syslog",
        "journald",
        "gelf",
        "fluentd",
        "awslogs",
        "splunk",
        "awsfirelens",
    )
)


def serialize_aws_json_1_1(value: LogDriver) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogDriver:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogDriver value: {data!r}")
    return cast(LogDriver, data)
