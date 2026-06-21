"""Generated from Smithy shape ``com.amazonaws.mediastoredata#StorageClass``."""

from typing import Literal, TypeAlias, cast

StorageClass: TypeAlias = Literal["TEMPORAL",]


# --- restJson1 ser/de ---
def serialize_json(value: StorageClass) -> str:
    return value


def deserialize_json(data: str) -> StorageClass:
    return cast(StorageClass, data)
