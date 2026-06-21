"""Generated from Smithy shape ``com.amazonaws.dlm#LocationValues``."""

from typing import Literal, TypeAlias, cast

LocationValues: TypeAlias = Literal[
    "CLOUD",
    "OUTPOST_LOCAL",
    "LOCAL_ZONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: LocationValues) -> str:
    return value


def deserialize_json(data: str) -> LocationValues:
    return cast(LocationValues, data)
