"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceSourceType``."""

from typing import Literal, TypeAlias, cast

ResourceSourceType: TypeAlias = Literal[
    "AppTemplate",
    "Discovered",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceSourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceSourceType:
    return cast(ResourceSourceType, data)
