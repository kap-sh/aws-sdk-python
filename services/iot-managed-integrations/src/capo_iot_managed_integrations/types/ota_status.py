"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#OtaStatus``."""

from typing import Literal, TypeAlias, cast

OtaStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELED",
    "COMPLETED",
    "DELETION_IN_PROGRESS",
    "SCHEDULED",
]


# --- restJson1 ser/de ---
def serialize_json(value: OtaStatus) -> str:
    return value


def deserialize_json(data: str) -> OtaStatus:
    return cast(OtaStatus, data)
