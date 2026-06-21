"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#SoftwareSetUpdateStatus``."""

from typing import Literal, TypeAlias, cast

SoftwareSetUpdateStatus: TypeAlias = Literal[
    "AVAILABLE",
    "IN_PROGRESS",
    "UP_TO_DATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareSetUpdateStatus) -> str:
    return value


def deserialize_json(data: str) -> SoftwareSetUpdateStatus:
    return cast(SoftwareSetUpdateStatus, data)
