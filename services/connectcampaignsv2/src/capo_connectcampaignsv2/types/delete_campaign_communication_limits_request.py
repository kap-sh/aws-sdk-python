"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignCommunicationLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.communication_limits_config_type


class DeleteCampaignCommunicationLimitsRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    config: "capo_connectcampaignsv2.types.communication_limits_config_type.CommunicationLimitsConfigType"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignCommunicationLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignCommunicationLimitsRequest:
    out: DeleteCampaignCommunicationLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
