"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ListConfiguredAudienceModelAssociationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_audience_model_association_summary_list
    import capo_cleanrooms.types.pagination_token


class ListConfiguredAudienceModelAssociationsOutput(TypedDict, closed=True):
    configured_audience_model_association_summaries: "capo_cleanrooms.types.configured_audience_model_association_summary_list.ConfiguredAudienceModelAssociationSummaryList"
    """<p>Summaries of the configured audience model associations that you requested.</p>"""
    next_token: NotRequired["capo_cleanrooms.types.pagination_token.PaginationToken"]
    """<p>The token value provided to access the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredAudienceModelAssociationsOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.configured_audience_model_association_summary_list

    out["configuredAudienceModelAssociationSummaries"] = (
        capo_cleanrooms.types.configured_audience_model_association_summary_list.serialize_json(
            value["configured_audience_model_association_summaries"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListConfiguredAudienceModelAssociationsOutput:
    out: ListConfiguredAudienceModelAssociationsOutput = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelAssociationSummaries" in data:
        import capo_cleanrooms.types.configured_audience_model_association_summary_list

        out["configured_audience_model_association_summaries"] = (
            capo_cleanrooms.types.configured_audience_model_association_summary_list.deserialize_json(
                data["configuredAudienceModelAssociationSummaries"]
            )
        )
    else:
        raise DeserializationError(
            "ListConfiguredAudienceModelAssociationsOutput.configured_audience_model_association_summaries required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
