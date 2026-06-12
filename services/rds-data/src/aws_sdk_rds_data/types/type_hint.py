"""Generated from Smithy shape ``com.amazonaws.rdsdata#TypeHint``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds_data.errors import DeserializationError

TypeHint: TypeAlias = Literal[
    "JSON",
    "UUID",
    "TIMESTAMP",
    "DATE",
    "TIME",
    "DECIMAL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "JSON",
        "UUID",
        "TIMESTAMP",
        "DATE",
        "TIME",
        "DECIMAL",
    )
)


def serialize_json(value: TypeHint) -> str:
    return value


def deserialize_json(data: str) -> TypeHint:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TypeHint value: {data!r}")
    return cast(TypeHint, data)
