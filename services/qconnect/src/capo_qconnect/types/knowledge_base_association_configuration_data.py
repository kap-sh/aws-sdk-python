"""Generated from Smithy shape ``com.amazonaws.qconnect#KnowledgeBaseAssociationConfigurationData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.knowledge_base_search_type
    import capo_qconnect.types.max_results
    import capo_qconnect.types.tag_filter


class KnowledgeBaseAssociationConfigurationData(TypedDict, closed=True):
    content_tag_filter: NotRequired["capo_qconnect.types.tag_filter.TagFilter"]
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    override_knowledge_base_search_type: NotRequired[
        "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
    ]
    """<p>The search type to be used against the Knowledge Base for this request. The values can be <code>SEMANTIC</code> which uses vector embeddings or <code>HYBRID</code> which use vector embeddings and raw text</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KnowledgeBaseAssociationConfigurationData) -> dict:
    out: dict = {}
    if "content_tag_filter" in value:
        import capo_qconnect.types.tag_filter

        out["contentTagFilter"] = capo_qconnect.types.tag_filter.serialize_json(
            value["content_tag_filter"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "override_knowledge_base_search_type" in value:
        out["overrideKnowledgeBaseSearchType"] = value[
            "override_knowledge_base_search_type"
        ]
    return out


def deserialize_json(data: dict) -> KnowledgeBaseAssociationConfigurationData:
    out: KnowledgeBaseAssociationConfigurationData = {}  # type: ignore[typeddict-item]
    if "contentTagFilter" in data:
        import capo_qconnect.types.tag_filter

        out["content_tag_filter"] = capo_qconnect.types.tag_filter.deserialize_json(
            data["contentTagFilter"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "overrideKnowledgeBaseSearchType" in data:
        out["override_knowledge_base_search_type"] = data[
            "overrideKnowledgeBaseSearchType"
        ]
    return out
