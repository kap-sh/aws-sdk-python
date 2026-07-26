"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#ListCampaignsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.campaign_summaries
    import capo_iotfleetwise.types.next_token


class ListCampaignsResponse(TypedDict, closed=True):
    campaign_summaries: NotRequired[
        "capo_iotfleetwise.types.campaign_summaries.campaignSummaries"
    ]
    """<p> A summary of information about each campaign. </p>"""
    next_token: NotRequired["capo_iotfleetwise.types.next_token.nextToken"]
    """<p> The token to retrieve the next set of results, or <code>null</code> if there are no more results. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListCampaignsResponse) -> dict:
    out: dict = {}
    if "campaign_summaries" in value:
        import capo_iotfleetwise.types.campaign_summaries

        out["campaignSummaries"] = (
            capo_iotfleetwise.types.campaign_summaries.serialize_aws_json_1_0(
                value["campaign_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListCampaignsResponse:
    out: ListCampaignsResponse = {}  # type: ignore[typeddict-item]
    if "campaignSummaries" in data:
        import capo_iotfleetwise.types.campaign_summaries

        out["campaign_summaries"] = (
            capo_iotfleetwise.types.campaign_summaries.deserialize_aws_json_1_0(
                data["campaignSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
