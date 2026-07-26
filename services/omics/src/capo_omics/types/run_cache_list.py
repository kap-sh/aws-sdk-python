"""Generated from Smithy shape ``com.amazonaws.omics#RunCacheList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_omics.types.run_cache_list_item

RunCacheList: TypeAlias = list["capo_omics.types.run_cache_list_item.RunCacheListItem"]


# --- restJson1 ser/de ---
def serialize_json(value: RunCacheList) -> list:
    import capo_omics.types.run_cache_list_item

    out: list = []
    for item in value:
        out.append(capo_omics.types.run_cache_list_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> RunCacheList:
    import capo_omics.types.run_cache_list_item

    out: RunCacheList = []
    for item in data:
        out.append(capo_omics.types.run_cache_list_item.deserialize_json(item))
    return out
