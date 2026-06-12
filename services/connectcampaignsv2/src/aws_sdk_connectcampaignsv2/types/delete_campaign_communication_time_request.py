"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignCommunicationTimeRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id
    import aws_sdk_connectcampaignsv2.types.communication_time_config_type


class DeleteCampaignCommunicationTimeRequest(TypedDict):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"
    config: "aws_sdk_connectcampaignsv2.types.communication_time_config_type.CommunicationTimeConfigType"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignCommunicationTimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignCommunicationTimeRequest:
    out: DeleteCampaignCommunicationTimeRequest = {}  # type: ignore[typeddict-item]
    return out
