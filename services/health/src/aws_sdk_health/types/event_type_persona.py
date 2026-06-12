"""Generated from Smithy shape ``com.amazonaws.health#EventTypePersona``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

EventTypePersona: TypeAlias = Literal[
    "OPERATIONS",
    "SECURITY",
    "BILLING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OPERATIONS",
        "SECURITY",
        "BILLING",
    )
)


def serialize_aws_json_1_1(value: EventTypePersona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventTypePersona:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventTypePersona value: {data!r}")
    return cast(EventTypePersona, data)
