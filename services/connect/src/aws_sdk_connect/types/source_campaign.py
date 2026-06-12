"""Generated from Smithy shape ``com.amazonaws.connect#SourceCampaign``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.campaign_id
    import aws_sdk_connect.types.outbound_request_id


class SourceCampaign(TypedDict):
    campaign_id: NotRequired["aws_sdk_connect.types.campaign_id.CampaignId"]
    """<p>A unique identifier for a campaign.</p>"""
    outbound_request_id: NotRequired[
        "aws_sdk_connect.types.outbound_request_id.OutboundRequestId"
    ]
    """<p>A unique identifier for a each request part of same campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceCampaign) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    if "outbound_request_id" in value:
        out["OutboundRequestId"] = value["outbound_request_id"]
    return out


def deserialize_json(data: dict) -> SourceCampaign:
    out: SourceCampaign = {}  # type: ignore[typeddict-item]
    if "CampaignId" in data:
        out["campaign_id"] = data["CampaignId"]
    if "OutboundRequestId" in data:
        out["outbound_request_id"] = data["OutboundRequestId"]
    return out
