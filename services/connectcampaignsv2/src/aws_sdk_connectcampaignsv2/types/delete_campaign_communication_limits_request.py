"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignCommunicationLimitsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.communication_limits_config_type


class DeleteCampaignCommunicationLimitsRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    config: "aws_sdk_connectcampaignsv2.types.communication_limits_config_type.CommunicationLimitsConfigType"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignCommunicationLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignCommunicationLimitsRequest:
    out: DeleteCampaignCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
