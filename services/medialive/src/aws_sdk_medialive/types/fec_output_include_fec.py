"""Generated from Smithy shape ``com.amazonaws.medialive#FecOutputIncludeFec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""Fec Output Include Fec"""
FecOutputIncludeFec: TypeAlias = Literal[
    "COLUMN",
    "COLUMN_AND_ROW",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COLUMN",
        "COLUMN_AND_ROW",
    )
)


def serialize_json(value: FecOutputIncludeFec) -> str:
    return value


def deserialize_json(data: str) -> FecOutputIncludeFec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FecOutputIncludeFec value: {data!r}")
    return cast(FecOutputIncludeFec, data)
