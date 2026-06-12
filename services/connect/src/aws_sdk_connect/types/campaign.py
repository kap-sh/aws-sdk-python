"""Generated from Smithy shape ``com.amazonaws.connect#Campaign``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.campaign_id


class Campaign(TypedDict):
    campaign_id: NotRequired["aws_sdk_connect.types.campaign_id.CampaignId"]
    """<p>A unique identifier for a campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Campaign) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["CampaignId"] = value["campaign_id"]
    return out


def deserialize_json(data: dict) -> Campaign:
    out: Campaign = {}  # type: ignore[typeddict-item]
    if "CampaignId" in data:
        out["campaign_id"] = data["CampaignId"]
    return out
