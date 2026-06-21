"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationQueryLogStatus``."""

from typing import Literal, TypeAlias, cast

CollaborationQueryLogStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationQueryLogStatus) -> str:
    return value


def deserialize_json(data: str) -> CollaborationQueryLogStatus:
    return cast(CollaborationQueryLogStatus, data)
