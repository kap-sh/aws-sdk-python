"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetCampaignStateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id


class GetCampaignStateRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignStateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCampaignStateRequest:
    out: GetCampaignStateRequest = {}  # type: ignore[typeddict-item]
    return out
