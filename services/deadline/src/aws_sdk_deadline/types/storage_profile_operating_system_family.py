"""Generated from Smithy shape ``com.amazonaws.deadline#StorageProfileOperatingSystemFamily``."""

from typing import Literal, TypeAlias, cast

StorageProfileOperatingSystemFamily: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
    "MACOS",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageProfileOperatingSystemFamily) -> str:
    return value


def deserialize_json(data: str) -> StorageProfileOperatingSystemFamily:
    return cast(StorageProfileOperatingSystemFamily, data)
