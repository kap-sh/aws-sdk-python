"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagCollectionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.tag_collection_filter

TagCollectionFilters: TypeAlias = list[
    "capo_devops_guru.types.tag_collection_filter.TagCollectionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagCollectionFilters) -> list:
    import capo_devops_guru.types.tag_collection_filter

    out: list = []
    for item in value:
        out.append(capo_devops_guru.types.tag_collection_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagCollectionFilters:
    import capo_devops_guru.types.tag_collection_filter

    out: TagCollectionFilters = []
    for item in data:
        out.append(capo_devops_guru.types.tag_collection_filter.deserialize_json(item))
    return out
