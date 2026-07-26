"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationIdNamespaceAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationIdNamespaceAssociationsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The token value provided to access the next page of results.</p>"""
    collaboration_id_namespace_association_summaries: "capo_cleanrooms.types.collaboration_id_namespace_association_summary_list.CollaborationIdNamespaceAssociationSummaryList"
    """<p>The summary information of the collaboration ID namespace associations that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCollaborationIdNamespaceAssociationsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary_list

    out["collaborationIdNamespaceAssociationSummaries"] = (
        capo_cleanrooms.types.collaboration_id_namespace_association_summary_list.serialize_json(
            value["collaboration_id_namespace_association_summaries"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListCollaborationIdNamespaceAssociationsOutput:
    out: ListCollaborationIdNamespaceAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "collaborationIdNamespaceAssociationSummaries" in data:
        import capo_cleanrooms.types.collaboration_id_namespace_association_summary_list

        out["collaboration_id_namespace_association_summaries"] = (
            capo_cleanrooms.types.collaboration_id_namespace_association_summary_list.deserialize_json(
                data["collaborationIdNamespaceAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationIdNamespaceAssociationsOutput.collaboration_id_namespace_association_summaries required"
        )
    return out
