"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignEntryLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id


class DeleteCampaignEntryLimitsRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignEntryLimitsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignEntryLimitsRequest:
    out: DeleteCampaignEntryLimitsRequest = {}  # type: ignore[typeddict-item]
    return out
