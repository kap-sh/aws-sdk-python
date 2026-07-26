"""Generated from Smithy shape ``com.amazonaws.wisdom#ListKnowledgeBasesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wisdom.types.knowledge_base_list
    import capo_wisdom.types.non_empty_string


class ListKnowledgeBasesResponse(TypedDict, closed=True):
    knowledge_base_summaries: "capo_wisdom.types.knowledge_base_list.KnowledgeBaseList"
    """<p>Information about the knowledge bases.</p>"""
    next_token: NotRequired["capo_wisdom.types.non_empty_string.NonEmptyString"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKnowledgeBasesResponse) -> dict:
    out: dict = {}
    import capo_wisdom.types.knowledge_base_list

    out["knowledgeBaseSummaries"] = (
        capo_wisdom.types.knowledge_base_list.serialize_json(
            value["knowledge_base_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListKnowledgeBasesResponse:
    out: ListKnowledgeBasesResponse = {}  # type: ignore[typeddict-item]
    if "knowledgeBaseSummaries" in data:
        import capo_wisdom.types.knowledge_base_list

        out["knowledge_base_summaries"] = (
            capo_wisdom.types.knowledge_base_list.deserialize_json(
                data["knowledgeBaseSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListKnowledgeBasesResponse.knowledge_base_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
