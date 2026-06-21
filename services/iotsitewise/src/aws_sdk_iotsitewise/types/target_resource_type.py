"""Generated from Smithy shape ``com.amazonaws.iotsitewise#TargetResourceType``."""

from typing import Literal, TypeAlias, cast

TargetResourceType: TypeAlias = Literal[
    "ASSET",
    "COMPUTATION_MODEL",
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetResourceType) -> str:
    return value


def deserialize_json(data: str) -> TargetResourceType:
    return cast(TargetResourceType, data)
