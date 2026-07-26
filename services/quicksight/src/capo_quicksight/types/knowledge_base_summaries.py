"""Generated from Smithy shape ``com.amazonaws.quicksight#KnowledgeBaseSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.knowledge_base_summary

KnowledgeBaseSummaries: TypeAlias = list[
    "capo_quicksight.types.knowledge_base_summary.KnowledgeBaseSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseSummaries) -> list:
    import capo_quicksight.types.knowledge_base_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.knowledge_base_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> KnowledgeBaseSummaries:
    import capo_quicksight.types.knowledge_base_summary

    out: KnowledgeBaseSummaries = []
    for item in data:
        out.append(capo_quicksight.types.knowledge_base_summary.deserialize_json(item))
    return out
