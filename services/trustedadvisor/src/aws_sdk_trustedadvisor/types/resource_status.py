"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

ResourceStatus: TypeAlias = Literal[
    "ok",
    "warning",
    "error",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceStatus:
    return cast(ResourceStatus, data)
