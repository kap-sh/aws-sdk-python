"""Generated from Smithy shape ``com.amazonaws.s3tables#TableBucketType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

TableBucketType: TypeAlias = Literal[
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


def serialize_json(value: TableBucketType) -> str:
    return value


def deserialize_json(data: str) -> TableBucketType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TableBucketType value: {data!r}")
    return cast(TableBucketType, data)
