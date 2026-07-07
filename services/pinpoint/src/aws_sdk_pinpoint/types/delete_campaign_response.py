"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaign_response


class DeleteCampaignResponse(TypedDict, closed=True):
    campaign_response: NotRequired[
        "aws_sdk_pinpoint.types.campaign_response.CampaignResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCampaignResponse) -> dict:
    out: dict = {}
    if "campaign_response" in value:
        import aws_sdk_pinpoint.types.campaign_response

        out["CampaignResponse"] = (
            aws_sdk_pinpoint.types.campaign_response.serialize_json(
                value["campaign_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteCampaignResponse:
    out: DeleteCampaignResponse = {}  # type: ignore[typeddict-item]
    if "CampaignResponse" in data:
        import aws_sdk_pinpoint.types.campaign_response

        out["campaign_response"] = (
            aws_sdk_pinpoint.types.campaign_response.deserialize_json(
                data["CampaignResponse"]
            )
        )
    return out
