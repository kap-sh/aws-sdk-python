"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#UpdateCampaignNameRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.campaign_name


class UpdateCampaignNameRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaigns.types.campaign_id.CampaignId"
    name: "aws_sdk_connectcampaigns.types.campaign_name.CampaignName"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignNameRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateCampaignNameRequest:
    out: UpdateCampaignNameRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateCampaignNameRequest.name required")
    return out
