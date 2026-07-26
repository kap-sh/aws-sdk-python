"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#ListCampaignsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_summary_list
    import capo_connectcampaignsv2.types.next_token


class ListCampaignsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_connectcampaignsv2.types.next_token.NextToken"]
    campaign_summary_list: NotRequired[
        "capo_connectcampaignsv2.types.campaign_summary_list.CampaignSummaryList"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ListCampaignsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "campaign_summary_list" in value:
        import capo_connectcampaignsv2.types.campaign_summary_list

        out["campaignSummaryList"] = (
            capo_connectcampaignsv2.types.campaign_summary_list.serialize_json(
                value["campaign_summary_list"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCampaignsResponse:
    out: ListCampaignsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "campaignSummaryList" in data:
        import capo_connectcampaignsv2.types.campaign_summary_list

        out["campaign_summary_list"] = (
            capo_connectcampaignsv2.types.campaign_summary_list.deserialize_json(
                data["campaignSummaryList"]
            )
        )
    return out
