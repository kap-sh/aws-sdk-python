"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskFailureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_outposts.errors import DeserializationError

CapacityTaskFailureType: TypeAlias = Literal[
    "UNSUPPORTED_CAPACITY_CONFIGURATION",
    "UNEXPECTED_ASSET_STATE",
    "BLOCKING_INSTANCES_NOT_EVACUATED",
    "INTERNAL_SERVER_ERROR",
    "RESOURCE_NOT_FOUND",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNSUPPORTED_CAPACITY_CONFIGURATION",
        "UNEXPECTED_ASSET_STATE",
        "BLOCKING_INSTANCES_NOT_EVACUATED",
        "INTERNAL_SERVER_ERROR",
        "RESOURCE_NOT_FOUND",
    )
)


def serialize_json(value: CapacityTaskFailureType) -> str:
    return value


def deserialize_json(data: str) -> CapacityTaskFailureType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityTaskFailureType value: {data!r}")
    return cast(CapacityTaskFailureType, data)
