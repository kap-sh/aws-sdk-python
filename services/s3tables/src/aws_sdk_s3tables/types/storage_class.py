"""Generated from Smithy shape ``com.amazonaws.s3tables#StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_s3tables.errors import DeserializationError

StorageClass: TypeAlias = Literal[
    "STANDARD",
    "INTELLIGENT_TIERING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "INTELLIGENT_TIERING",
    )
)


def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {data!r}")
    return cast(StorageClass, data)
