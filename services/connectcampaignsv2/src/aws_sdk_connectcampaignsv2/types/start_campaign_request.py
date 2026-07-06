"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#StartCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id


class StartCampaignRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: StartCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartCampaignRequest:
    out: StartCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
