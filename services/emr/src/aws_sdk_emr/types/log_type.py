"""Generated from Smithy shape ``com.amazonaws.emr#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

LogType: TypeAlias = Literal[
    "system-logs",
    "application-logs",
    "persistent-ui-logs",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "system-logs",
        "application-logs",
        "persistent-ui-logs",
    )
)


def serialize_aws_json_1_1(value: LogType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
