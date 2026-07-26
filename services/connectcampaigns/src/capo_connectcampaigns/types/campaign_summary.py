"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_arn
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.campaign_name
    import capo_connectcampaigns.types.instance_id


class CampaignSummary(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"
    arn: "capo_connectcampaigns.types.campaign_arn.CampaignArn"
    name: "capo_connectcampaigns.types.campaign_name.CampaignName"
    connect_instance_id: "capo_connectcampaigns.types.instance_id.InstanceId"


# --- restJson1 ser/de ---
def serialize_json(value: CampaignSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["connectInstanceId"] = value["connect_instance_id"]
    return out


def deserialize_json(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CampaignSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CampaignSummary.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CampaignSummary.name required")
    if "connectInstanceId" in data:
        out["connect_instance_id"] = data["connectInstanceId"]
    else:
        raise DeserializationError("CampaignSummary.connect_instance_id required")
    return out
