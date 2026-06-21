"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DELETED",
    "DEPRECATED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
