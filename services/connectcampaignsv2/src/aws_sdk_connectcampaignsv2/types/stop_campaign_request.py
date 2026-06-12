"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#StopCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id


class StopCampaignRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: StopCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopCampaignRequest:
    out: StopCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
