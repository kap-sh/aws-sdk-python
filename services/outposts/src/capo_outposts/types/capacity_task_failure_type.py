"""Generated from Smithy shape ``com.amazonaws.outposts#CapacityTaskFailureType``."""

from typing import Literal, TypeAlias, cast

CapacityTaskFailureType: TypeAlias = Literal[
    "UNSUPPORTED_CAPACITY_CONFIGURATION",
    "UNEXPECTED_ASSET_STATE",
    "BLOCKING_INSTANCES_NOT_EVACUATED",
    "INTERNAL_SERVER_ERROR",
    "RESOURCE_NOT_FOUND",
]


# --- restJson1 ser/de ---
def serialize_json(value: CapacityTaskFailureType) -> str:
    return value


def deserialize_json(data: str) -> CapacityTaskFailureType:
    return cast(CapacityTaskFailureType, data)
