"""Generated from Smithy shape ``com.amazonaws.backup#RestoreDeletionStatus``."""

from typing import Literal, TypeAlias, cast

RestoreDeletionStatus: TypeAlias = Literal[
    "DELETING",
    "FAILED",
    "SUCCESSFUL",
]


# --- restJson1 ser/de ---
def serialize_json(value: RestoreDeletionStatus) -> str:
    return value


def deserialize_json(data: str) -> RestoreDeletionStatus:
    return cast(RestoreDeletionStatus, data)
