"""Generated from Smithy shape ``com.amazonaws.batch#LogDriver``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_batch.errors import DeserializationError

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


def serialize_json(value: LogDriver) -> str:
    return value


def deserialize_json(data: str) -> LogDriver:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogDriver value: {data!r}")
    return cast(LogDriver, data)
