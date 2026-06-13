"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergNullOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

IcebergNullOrder: TypeAlias = Literal[
    "nulls-first",
    "nulls-last",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "nulls-first",
        "nulls-last",
    )
)


def serialize_json(value: IcebergNullOrder) -> str:
    return value


def deserialize_json(data: str) -> IcebergNullOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergNullOrder value: {data!r}")
    return cast(IcebergNullOrder, data)
