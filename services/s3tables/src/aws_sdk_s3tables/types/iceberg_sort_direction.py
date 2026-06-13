"""Generated from Smithy shape ``com.amazonaws.s3tables#IcebergSortDirection``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

IcebergSortDirection: TypeAlias = Literal[
    "asc",
    "desc",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "asc",
        "desc",
    )
)


def serialize_json(value: IcebergSortDirection) -> str:
    return value


def deserialize_json(data: str) -> IcebergSortDirection:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IcebergSortDirection value: {data!r}")
    return cast(IcebergSortDirection, data)
