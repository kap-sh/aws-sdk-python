"""Generated from Smithy shape ``com.amazonaws.ram#ResourceShareFeatureSet``."""

from typing import Literal, TypeAlias, cast

ResourceShareFeatureSet: TypeAlias = Literal[
    "CREATED_FROM_POLICY",
    "PROMOTING_TO_STANDARD",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareFeatureSet) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareFeatureSet:
    return cast(ResourceShareFeatureSet, data)
