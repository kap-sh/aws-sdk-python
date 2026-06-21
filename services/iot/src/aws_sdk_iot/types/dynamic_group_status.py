"""Generated from Smithy shape ``com.amazonaws.iot#DynamicGroupStatus``."""

from typing import Literal, TypeAlias, cast

DynamicGroupStatus: TypeAlias = Literal[
    "ACTIVE",
    "BUILDING",
    "REBUILDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: DynamicGroupStatus) -> str:
    return value


def deserialize_json(data: str) -> DynamicGroupStatus:
    return cast(DynamicGroupStatus, data)
