"""Generated from Smithy shape ``com.amazonaws.glacier#StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glacier.errors import DeserializationError

StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "REDUCED_REDUNDANCY",
        "STANDARD_IA",
    )
)


def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {data!r}")
    return cast(StorageClass, data)
