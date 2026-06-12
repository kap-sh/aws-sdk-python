"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateCampaignRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.write_campaign_request


class UpdateCampaignRequest(TypedDict):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    campaign_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the campaign.</p>"""
    write_campaign_request: NotRequired[
        "aws_sdk_pinpoint.types.write_campaign_request.WriteCampaignRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCampaignRequest) -> dict:
    out: dict = {}
    if "write_campaign_request" in value:
        import aws_sdk_pinpoint.types.write_campaign_request

        out["WriteCampaignRequest"] = (
            aws_sdk_pinpoint.types.write_campaign_request.serialize_json(
                value["write_campaign_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCampaignRequest:
    out: UpdateCampaignRequest = {}  # type: ignore[typeddict-item]
    if "WriteCampaignRequest" in data:
        import aws_sdk_pinpoint.types.write_campaign_request

        out["write_campaign_request"] = (
            aws_sdk_pinpoint.types.write_campaign_request.deserialize_json(
                data["WriteCampaignRequest"]
            )
        )
    return out
