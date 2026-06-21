"""Generated from Smithy shape ``com.amazonaws.workdocs#StorageType``."""

from typing import Literal, TypeAlias, cast

StorageType: TypeAlias = Literal[
    "UNLIMITED",
    "QUOTA",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageType) -> str:
    return value


def deserialize_json(data: str) -> StorageType:
    return cast(StorageType, data)
