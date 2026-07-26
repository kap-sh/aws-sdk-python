"""Generated from Smithy shape ``com.amazonaws.opensearch#StorageTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.storage_type

StorageTypeList: TypeAlias = list["capo_opensearch.types.storage_type.StorageType"]


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeList) -> list:
    import capo_opensearch.types.storage_type

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.storage_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> StorageTypeList:
    import capo_opensearch.types.storage_type

    out: StorageTypeList = []
    for item in data:
        out.append(capo_opensearch.types.storage_type.deserialize_json(item))
    return out
