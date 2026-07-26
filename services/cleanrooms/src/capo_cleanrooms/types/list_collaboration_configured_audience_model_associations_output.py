"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListCollaborationConfiguredAudienceModelAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list
    import capo_cleanrooms.types.pagination_token


class ListCollaborationConfiguredAudienceModelAssociationsOutput(
    TypedDict, closed=True
):
    collaboration_configured_audience_model_association_summaries: "capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list.CollaborationConfiguredAudienceModelAssociationSummaryList"
    """<p>The metadata of the configured audience model association within a collaboration.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The pagination token that's used to fetch the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: ListCollaborationConfiguredAudienceModelAssociationsOutput,
) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list

    out["collaborationConfiguredAudienceModelAssociationSummaries"] = (
        capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list.serialize_json(
            value["collaboration_configured_audience_model_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(
    data: dict,
) -> ListCollaborationConfiguredAudienceModelAssociationsOutput:
    out: ListCollaborationConfiguredAudienceModelAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "collaborationConfiguredAudienceModelAssociationSummaries" in data:
        import capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list

        out["collaboration_configured_audience_model_association_summaries"] = (
            capo_cleanrooms.types.collaboration_configured_audience_model_association_summary_list.deserialize_json(
                data["collaborationConfiguredAudienceModelAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListCollaborationConfiguredAudienceModelAssociationsOutput.collaboration_configured_audience_model_association_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
