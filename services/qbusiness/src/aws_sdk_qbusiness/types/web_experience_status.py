"""Generated from Smithy shape ``com.amazonaws.qbusiness#WebExperienceStatus``."""

from typing import Literal, TypeAlias, cast

WebExperienceStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "DELETING",
    "FAILED",
    "PENDING_AUTH_CONFIG",
]


# --- restJson1 ser/de ---
def serialize_json(value: WebExperienceStatus) -> str:
    return value


def deserialize_json(data: str) -> WebExperienceStatus:
    return cast(WebExperienceStatus, data)
