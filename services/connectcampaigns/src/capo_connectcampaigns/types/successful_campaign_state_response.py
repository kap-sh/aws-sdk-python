"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#SuccessfulCampaignStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.campaign_state


class SuccessfulCampaignStateResponse(TypedDict, closed=True):
    campaign_id: NotRequired["capo_connectcampaigns.types.campaign_id.CampaignId"]
    state: NotRequired["capo_connectcampaigns.types.campaign_state.CampaignState"]


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
