"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#LogType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotfleetwise.errors import DeserializationError

LogType: TypeAlias = Literal[
    "OFF",
    "ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OFF",
        "ERROR",
    )
)


def serialize_aws_json_1_0(value: LogType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LogType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogType value: {data!r}")
    return cast(LogType, data)
