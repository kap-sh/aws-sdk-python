"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSearchFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.knowledge_base_search_filter

KnowledgeBaseSearchFilters: TypeAlias = list[
    "aws_sdk_quicksight.types.knowledge_base_search_filter.KnowledgeBaseSearchFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSearchFilters) -> list:
    import aws_sdk_quicksight.types.knowledge_base_search_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.knowledge_base_search_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> KnowledgeBaseSearchFilters:
    import aws_sdk_quicksight.types.knowledge_base_search_filter

    out: KnowledgeBaseSearchFilters = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.knowledge_base_search_filter.deserialize_json(item)
        )
    return out
