"""Generated from Smithy shape ``com.amazonaws.ssmsap#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationStatus: TypeAlias = Literal[
    "ACTIVATED",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "FAILED",
    "REGISTERING",
    "DELETING",
    "UNKNOWN",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
