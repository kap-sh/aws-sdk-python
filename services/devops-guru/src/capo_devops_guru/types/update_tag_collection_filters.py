"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateTagCollectionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.update_tag_collection_filter

UpdateTagCollectionFilters: TypeAlias = list[
    "capo_devops_guru.types.update_tag_collection_filter.UpdateTagCollectionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTagCollectionFilters) -> list:
    import capo_devops_guru.types.update_tag_collection_filter

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.update_tag_collection_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpdateTagCollectionFilters:
    import capo_devops_guru.types.update_tag_collection_filter

    out: UpdateTagCollectionFilters = []
    for item in data:
        out.append(
            capo_devops_guru.types.update_tag_collection_filter.deserialize_json(item)
        )
    return out
