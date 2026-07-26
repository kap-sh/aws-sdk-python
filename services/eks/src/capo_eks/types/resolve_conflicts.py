"""Generated from Smithy shape ``com.amazonaws.eks#ResolveConflicts``."""

from typing import Literal, TypeAlias, cast

ResolveConflicts: TypeAlias = Literal[
    "OVERWRITE",
    "NONE",
    "PRESERVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResolveConflicts) -> str:
    return value


def deserialize_json(data: str) -> ResolveConflicts:
    return cast(ResolveConflicts, data)
