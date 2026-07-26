"""Generated from Smithy shape ``com.amazonaws.wisdom#KnowledgeBaseList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_wisdom.types.knowledge_base_summary

KnowledgeBaseList: TypeAlias = list[
    "capo_wisdom.types.knowledge_base_summary.KnowledgeBaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseList) -> list:
    import capo_wisdom.types.knowledge_base_summary

    out: list = []
    for item in value:
        out.append(capo_wisdom.types.knowledge_base_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> KnowledgeBaseList:
    import capo_wisdom.types.knowledge_base_summary

    out: KnowledgeBaseList = []
    for item in data:
        out.append(capo_wisdom.types.knowledge_base_summary.deserialize_json(item))
    return out
