"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string


class GetCampaignVersionRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    campaign_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the campaign.</p>"""
    version: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique version number (Version property) for the campaign version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignVersionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCampaignVersionRequest:
    out: GetCampaignVersionRequest = {}  # type: ignore[typeddict-item]
    return out
