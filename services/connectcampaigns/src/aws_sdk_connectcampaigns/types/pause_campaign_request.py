"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#PauseCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id


class PauseCampaignRequest(TypedDict):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: PauseCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PauseCampaignRequest:
    out: PauseCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
