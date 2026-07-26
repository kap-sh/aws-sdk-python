"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignCommunicationTimeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.communication_time_config_type


class DeleteCampaignCommunicationTimeRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    config: "capo_connectcampaignsv2.types.communication_time_config_type.CommunicationTimeConfigType"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignCommunicationTimeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignCommunicationTimeRequest:
    out: DeleteCampaignCommunicationTimeRequest = {}  # type: ignore[typeddict-item]
    return out
