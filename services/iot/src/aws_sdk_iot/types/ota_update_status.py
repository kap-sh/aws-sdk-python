"""Generated from Smithy shape ``com.amazonaws.iot#OTAUpdateStatus``."""

from typing import Literal, TypeAlias, cast

OTAUpdateStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_COMPLETE",
    "CREATE_FAILED",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OTAUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> OTAUpdateStatus:
    return cast(OTAUpdateStatus, data)
