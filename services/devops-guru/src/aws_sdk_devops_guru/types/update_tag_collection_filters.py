"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateTagCollectionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.update_tag_collection_filter

UpdateTagCollectionFilters: TypeAlias = list[
    "aws_sdk_devops_guru.types.update_tag_collection_filter.UpdateTagCollectionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTagCollectionFilters) -> list:
    import aws_sdk_devops_guru.types.update_tag_collection_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.update_tag_collection_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UpdateTagCollectionFilters:
    import aws_sdk_devops_guru.types.update_tag_collection_filter

    out: UpdateTagCollectionFilters = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.update_tag_collection_filter.deserialize_json(
                item
            )
        )
    return out
