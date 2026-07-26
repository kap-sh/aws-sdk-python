"""Generated from Smithy shape ``com.amazonaws.glacier#StorageClass``."""

from typing import Literal, TypeAlias, cast

StorageClass: TypeAlias = Literal[
    "STANDARD",
    "REDUCED_REDUNDANCY",
    "STANDARD_IA",
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    return cast(StorageClass, data)
