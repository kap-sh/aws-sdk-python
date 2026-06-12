"""Generated from Smithy shape ``com.amazonaws.applicationinsights#LogFilter``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

LogFilter: TypeAlias = Literal[
    "ERROR",
    "WARN",
    "INFO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ERROR",
        "WARN",
        "INFO",
    )
)


def serialize_aws_json_1_1(value: LogFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogFilter:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogFilter value: {data!r}")
    return cast(LogFilter, data)
