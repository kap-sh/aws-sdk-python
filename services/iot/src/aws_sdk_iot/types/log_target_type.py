"""Generated from Smithy shape ``com.amazonaws.iot#LogTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

LogTargetType: TypeAlias = Literal[
    "DEFAULT",
    "THING_GROUP",
    "CLIENT_ID",
    "SOURCE_IP",
    "PRINCIPAL_ID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "THING_GROUP",
        "CLIENT_ID",
        "SOURCE_IP",
        "PRINCIPAL_ID",
    )
)


def serialize_json(value: LogTargetType) -> str:
    return value


def deserialize_json(data: str) -> LogTargetType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown LogTargetType value: {data!r}")
    return cast(LogTargetType, data)
