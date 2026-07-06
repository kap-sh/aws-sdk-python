"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#DeleteCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.campaign_id


class DeleteCampaignRequest(TypedDict, closed=True):
    id: "aws_sdk_connectcampaignsv2.types.campaign_id.CampaignId"


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCampaignRequest:
    out: DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
