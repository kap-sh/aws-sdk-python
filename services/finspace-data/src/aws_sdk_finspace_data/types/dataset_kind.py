"""Generated from Smithy shape ``com.amazonaws.finspacedata#DatasetKind``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Dataset Kind"""
DatasetKind: TypeAlias = Literal[
    "TABULAR",
    "NON_TABULAR",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "TABULAR",
        "NON_TABULAR",
    )
)


def serialize_json(value: DatasetKind) -> str:
    return value


def deserialize_json(data: str) -> DatasetKind:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DatasetKind value: {data!r}")
    return cast(DatasetKind, data)
