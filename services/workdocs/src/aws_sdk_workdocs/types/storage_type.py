"""Generated from Smithy shape ``com.amazonaws.workdocs#StorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workdocs.errors import DeserializationError

StorageType: TypeAlias = Literal[
    "UNLIMITED",
    "QUOTA",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UNLIMITED",
        "QUOTA",
    )
)


def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StorageType value: {data!r}")
    return cast(StorageType, data)
