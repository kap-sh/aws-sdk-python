"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetKind``."""

from typing import Literal, TypeAlias, cast

"""Dataset Kind"""
DatasetKind: TypeAlias = Literal[
    "TABULAR",
    "NON_TABULAR",
]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetKind) -> str:
    return value


def deserialize_json(data: str) -> DatasetKind:
    return cast(DatasetKind, data)
