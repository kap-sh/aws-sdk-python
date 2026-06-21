"""Generated from Smithy shape ``com.amazonaws.finspacedata#ChangeType``."""

from typing import Literal, TypeAlias, cast

"""Indicates how the given change will be applied to the dataset."""
ChangeType: TypeAlias = Literal[
    "REPLACE",
    "APPEND",
    "MODIFY",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    return cast(ChangeType, data)
