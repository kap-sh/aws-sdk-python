"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceResolutionStatusType``."""

from typing import Literal, TypeAlias, cast

ResourceResolutionStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceResolutionStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourceResolutionStatusType:
    return cast(ResourceResolutionStatusType, data)
