"""Generated from Smithy shape ``com.amazonaws.backup#StorageClass``."""

from typing import Literal, TypeAlias, cast

StorageClass: TypeAlias = Literal[
    "WARM",
    "COLD",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    return cast(StorageClass, data)
