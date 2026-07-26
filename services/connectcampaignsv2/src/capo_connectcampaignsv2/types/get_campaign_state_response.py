"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#GetCampaignStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_state


class GetCampaignStateResponse(TypedDict, closed=True):
    state: NotRequired["capo_connectcampaignsv2.types.campaign_state.CampaignState"]


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignStateResponse) -> dict:
    out: dict = {}
    if "state" in value:
        out["state"] = value["state"]
    return out


def deserialize_json(data: dict) -> GetCampaignStateResponse:
    out: GetCampaignStateResponse = {}  # type: ignore[typeddict-item]
    if "state" in data:
        out["state"] = data["state"]
    return out
