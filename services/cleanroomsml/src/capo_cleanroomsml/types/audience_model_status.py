"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceModelStatus``."""

from typing import Literal, TypeAlias, cast

AudienceModelStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "CREATE_IN_PROGRESS",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETE_PENDING",
    "DELETE_IN_PROGRESS",
    "DELETE_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceModelStatus) -> str:
    return value


def deserialize_json(data: str) -> AudienceModelStatus:
    return cast(AudienceModelStatus, data)
