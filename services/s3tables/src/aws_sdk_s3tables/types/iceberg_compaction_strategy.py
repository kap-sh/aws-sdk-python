"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergCompactionStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

IcebergCompactionStrategy: TypeAlias = Literal[
    "auto",
    "binpack",
    "sort",
    "z-order",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "auto",
        "binpack",
        "sort",
        "z-order",
    )
)


def serialize_json(value: IcebergCompactionStrategy) -> str:
    return value


def deserialize_json(data: str) -> IcebergCompactionStrategy:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergCompactionStrategy value: {data!r}")
    return cast(IcebergCompactionStrategy, data)
