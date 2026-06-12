"""Generated from Smithy shape ``com.amazonaws.deadline#StorageProfileOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_deadline.errors import DeserializationError

StorageProfileOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
    "MACOS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "WINDOWS",
        "LINUX",
        "MACOS",
    )
)


def serialize_json(value: StorageProfileOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> StorageProfileOperatingSystemFamily:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown StorageProfileOperatingSystemFamily value: {data!r}"
        )
    return cast(StorageProfileOperatingSystemFamily, data)
