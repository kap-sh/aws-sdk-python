"""Generated from Smithy shape ``com.amazonaws.finspace#KxSavedownStorageType``."""

from typing import Literal, TypeAlias, cast

KxSavedownStorageType: TypeAlias = Literal["SDS01",]


# --- restJson1 ser/de ---
def serialize_json(value: KxSavedownStorageType) -> str:
    return value


def deserialize_json(data: str) -> KxSavedownStorageType:
    return cast(KxSavedownStorageType, data)
