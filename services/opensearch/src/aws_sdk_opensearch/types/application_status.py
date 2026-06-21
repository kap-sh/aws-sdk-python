"""Generated from Smithy shape ``com.amazonaws.opensearch#ApplicationStatus``."""

from typing import Literal, TypeAlias, cast

ApplicationStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "DELETING",
    "ACTIVE",
    "FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationStatus) -> str:
    return value


def deserialize_json(data: str) -> ApplicationStatus:
    return cast(ApplicationStatus, data)
