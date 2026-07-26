"""Generated from Smithy shape ``com.amazonaws.connectparticipant#ArtifactStatus``."""

from typing import Literal, TypeAlias, cast

ArtifactStatus: TypeAlias = Literal[
    "APPROVED",
    "REJECTED",
    "IN_PROGRESS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ArtifactStatus) -> str:
    return value


def deserialize_json(data: str) -> ArtifactStatus:
    return cast(ArtifactStatus, data)
