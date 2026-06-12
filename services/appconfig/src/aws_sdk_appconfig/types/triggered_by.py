"""Generated from Smithy shape ``com.amazonaws.appconfig#TriggeredBy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

TriggeredBy: TypeAlias = Literal[
    "USER",
    "APPCONFIG",
    "CLOUDWATCH_ALARM",
    "INTERNAL_ERROR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "APPCONFIG",
        "CLOUDWATCH_ALARM",
        "INTERNAL_ERROR",
    )
)


def serialize_json(value: TriggeredBy) -> str:
    return value


def deserialize_json(data: str) -> TriggeredBy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TriggeredBy value: {data!r}")
    return cast(TriggeredBy, data)
