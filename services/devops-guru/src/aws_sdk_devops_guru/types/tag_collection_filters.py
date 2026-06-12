"""Generated from Smithy shape ``com.amazonaws.devopsguru#TagCollectionFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.tag_collection_filter

TagCollectionFilters: TypeAlias = list[
    "aws_sdk_devops_guru.types.tag_collection_filter.TagCollectionFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagCollectionFilters) -> list:
    import aws_sdk_devops_guru.types.tag_collection_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.tag_collection_filter.serialize_json(item))
    return out


def deserialize_json(data: list) -> TagCollectionFilters:
    import aws_sdk_devops_guru.types.tag_collection_filter

    out: TagCollectionFilters = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.tag_collection_filter.deserialize_json(item)
        )
    return out
