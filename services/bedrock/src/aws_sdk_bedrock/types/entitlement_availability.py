"""Generated from Smithy shape ``com.amazonaws.bedrock#EntitlementAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

EntitlementAvailability: TypeAlias = Literal[
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "NOT_AVAILABLE",
    )
)


def serialize_json(value: EntitlementAvailability) -> str:
    return value


def deserialize_json(data: str) -> EntitlementAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntitlementAvailability value: {data!r}")
    return cast(EntitlementAvailability, data)
