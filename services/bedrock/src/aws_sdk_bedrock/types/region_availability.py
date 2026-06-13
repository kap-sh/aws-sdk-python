"""Generated from Smithy shape ``com.amazonaws.bedrock#RegionAvailability``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

RegionAvailability: TypeAlias = Literal[
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


def serialize_json(value: RegionAvailability) -> str:
    return value


def deserialize_json(data: str) -> RegionAvailability:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RegionAvailability value: {data!r}")
    return cast(RegionAvailability, data)
