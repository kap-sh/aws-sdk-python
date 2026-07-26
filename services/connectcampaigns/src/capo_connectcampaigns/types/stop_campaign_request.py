"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#StopCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_id


class StopCampaignRequest(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: StopCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCampaignRequest:
    out: StopCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
