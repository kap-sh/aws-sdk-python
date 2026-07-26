"""Generated from Smithy shape ``com.amazonaws.ram#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "ZONAL_RESOURCE_INACCESSIBLE",
    "LIMIT_EXCEEDED",
    "UNAVAILABLE",
    "PENDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
