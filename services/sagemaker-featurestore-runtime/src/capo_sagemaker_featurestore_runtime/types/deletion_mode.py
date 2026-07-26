"""Generated from Smithy shape ``com.amazonaws.sagemakerfeaturestoreruntime#DeletionMode``."""

from typing import Literal, TypeAlias, cast

DeletionMode: TypeAlias = Literal[
    "SoftDelete",
    "HardDelete",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeletionMode) -> str:
    return value


def deserialize_json(data: str) -> DeletionMode:
    return cast(DeletionMode, data)
