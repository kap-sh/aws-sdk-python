"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignChannelSubtypeConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.channel_subtype


class DeleteCampaignChannelSubtypeConfigRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    channel_subtype: "capo_connectcampaignsv2.types.channel_subtype.ChannelSubtype"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignChannelSubtypeConfigRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignChannelSubtypeConfigRequest:
    out: DeleteCampaignChannelSubtypeConfigRequest = {}  # type: ignore[typeddict-item]
    return out
