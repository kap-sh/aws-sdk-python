"""Generated from Smithy shape ``com.amazonaws.health#EventPersona``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_health.errors import DeserializationError

EventPersona: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: EventPersona) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EventPersona:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EventPersona value: {data!r}")
    return cast(EventPersona, data)
