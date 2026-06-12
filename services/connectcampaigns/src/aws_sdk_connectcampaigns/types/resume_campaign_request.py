"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#ResumeCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id


class ResumeCampaignRequest(TypedDict):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: ResumeCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ResumeCampaignRequest:
    out: ResumeCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
