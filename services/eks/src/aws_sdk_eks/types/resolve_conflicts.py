"""Generated from Smithy shape ``com.amazonaws.eks#ResolveConflicts``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_eks.errors import DeserializationError

ResolveConflicts: TypeAlias = Literal[
    "OVERWRITE",
    "NONE",
    "PRESERVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OVERWRITE",
        "NONE",
        "PRESERVE",
    )
)


def serialize_json(value: ResolveConflicts) -> str:
    return value


def deserialize_json(data: str) -> ResolveConflicts:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResolveConflicts value: {data!r}")
    return cast(ResolveConflicts, data)
