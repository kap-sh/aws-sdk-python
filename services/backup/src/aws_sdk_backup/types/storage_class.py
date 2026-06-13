"""Generated from Smithy shape ``com.amazonaws.backup#StorageClass``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_backup.errors import DeserializationError

StorageClass: TypeAlias = Literal[
    "WARM",
    "COLD",
    "DELETED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WARM",
        "COLD",
        "DELETED",
    )
)


def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageClass value: {data!r}")
    return cast(StorageClass, data)
