"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceLocationValues``."""

from typing import Literal, TypeAlias, cast

ResourceLocationValues: TypeAlias = Literal[
    "CLOUD",
    "OUTPOST",
    "LOCAL_ZONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLocationValues) -> str:
    return value


def deserialize_json(data: str) -> ResourceLocationValues:
    return cast(ResourceLocationValues, data)
