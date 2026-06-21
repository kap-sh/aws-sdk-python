"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationJobLogStatus``."""

from typing import Literal, TypeAlias, cast

CollaborationJobLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationJobLogStatus) -> str:
    return value


def deserialize_json(data: str) -> CollaborationJobLogStatus:
    return cast(CollaborationJobLogStatus, data)
