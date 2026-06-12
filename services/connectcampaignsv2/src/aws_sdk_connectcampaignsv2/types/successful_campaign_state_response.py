"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#SuccessfulCampaignStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.campaign_state


class SuccessfulCampaignStateResponse(TypedDict):
    campaign_id: NotRequired["aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"]
    state: NotRequired["aws_sdk_connectcampaignsv2.types.campaign_state.CampaignState"]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulCampaignStateResponse) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["campaignId"] = value["campaign_id"]
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> SuccessfulCampaignStateResponse:
    out: SuccessfulCampaignStateResponse = {}  # type: ignore[typeddict-item]
    if "campaignId" in data:
        out["campaign_id"] = data["campaignId"]
    if "state" in data:
        out["state"] = data["state"]
    return out
