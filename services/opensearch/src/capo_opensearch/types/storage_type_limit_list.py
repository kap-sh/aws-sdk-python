"""Generated from Smithy shape ``com.amazonaws.opensearch#StorageTypeLimitList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_opensearch.types.storage_type_limit

StorageTypeLimitList: TypeAlias = list[
    "capo_opensearch.types.storage_type_limit.StorageTypeLimit"
]


# --- restJson1 ser/de ---
def serialize_json(value: StorageTypeLimitList) -> list:
    import capo_opensearch.types.storage_type_limit

    out: list = []
    for item in value:
        out.append(capo_opensearch.types.storage_type_limit.serialize_json(item))
    return out


def deserialize_json(data: list) -> StorageTypeLimitList:
    import capo_opensearch.types.storage_type_limit

    out: StorageTypeLimitList = []
    for item in data:
        out.append(capo_opensearch.types.storage_type_limit.deserialize_json(item))
    return out
