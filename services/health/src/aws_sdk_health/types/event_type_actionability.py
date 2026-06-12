"""Generated from Smithy shape ``com.amazonaws.health#EventTypeActionability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

EventTypeActionability: TypeAlias = Literal[
    "ACTION_REQUIRED",
    "ACTION_MAY_BE_REQUIRED",
    "INFORMATIONAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTION_REQUIRED",
        "ACTION_MAY_BE_REQUIRED",
        "INFORMATIONAL",
    )
)


def serialize_aws_json_1_1(value: EventTypeActionability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventTypeActionability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventTypeActionability value: {data!r}")
    return cast(EventTypeActionability, data)
