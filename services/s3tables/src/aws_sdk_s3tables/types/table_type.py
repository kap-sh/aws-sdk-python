"""Generated from Smithy shape ``com.amazonaws.s3tables#TableType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableType: TypeAlias = Literal[
    "customer",
    "aws",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "customer",
        "aws",
    )
)


def serialize_json(value: TableType) -> str:
    return value


def deserialize_json(data: str) -> TableType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableType value: {data!r}")
    return cast(TableType, data)
