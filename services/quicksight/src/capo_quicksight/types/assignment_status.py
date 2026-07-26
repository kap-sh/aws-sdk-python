"""Generated from Smithy shape ``com.amazonaws.quicksight#AssignmentStatus``."""

from typing import Literal, TypeAlias, cast

AssignmentStatus: TypeAlias = Literal[
    "ENABLED",
    "DRAFT",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: AssignmentStatus) -> str:
    return value


def deserialize_json(data: str) -> AssignmentStatus:
    return cast(AssignmentStatus, data)
