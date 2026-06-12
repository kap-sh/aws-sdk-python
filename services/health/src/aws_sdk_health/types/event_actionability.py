"""Generated from Smithy shape ``com.amazonaws.health#EventActionability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

EventActionability: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: EventActionability) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventActionability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventActionability value: {data!r}")
    return cast(EventActionability, data)
