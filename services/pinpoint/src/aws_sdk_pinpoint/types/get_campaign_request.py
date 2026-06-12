"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetCampaignRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    campaign_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the campaign.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCampaignRequest:
    out: GetCampaignRequest = {}  # type: ignore[typeddict-item]
    return out
