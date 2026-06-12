"""Generated from Smithy shape ``com.amazonaws.finspacedata#ChangeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_finspace_data.errors import DeserializationError

"""Indicates how the given change will be applied to the dataset."""
ChangeType: TypeAlias = Literal[
    "REPLACE",
    "APPEND",
    "MODIFY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPLACE",
        "APPEND",
        "MODIFY",
    )
)


def serialize_json(value: ChangeType) -> str:
    return value


def deserialize_json(data: str) -> ChangeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChangeType value: {data!r}")
    return cast(ChangeType, data)
