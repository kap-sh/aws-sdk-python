"""Generated from Smithy shape ``com.amazonaws.gameliftstreams#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationStatus: TypeAlias = Literal[
    "INITIALIZED",
    "PROCESSING",
    "READY",
    "DELETING",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
