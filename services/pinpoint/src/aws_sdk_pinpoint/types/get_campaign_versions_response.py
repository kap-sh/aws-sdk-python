"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaigns_response


class GetCampaignVersionsResponse(TypedDict, closed=True):
    campaigns_response: NotRequired[
        "aws_sdk_pinpoint.types.campaigns_response.CampaignsResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignVersionsResponse) -> dict:
    out: dict = {}
    if "campaigns_response" in value:
        import aws_sdk_pinpoint.types.campaigns_response

        out["CampaignsResponse"] = (
            aws_sdk_pinpoint.types.campaigns_response.serialize_json(
                value["campaigns_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetCampaignVersionsResponse:
    out: GetCampaignVersionsResponse = {}  # type: ignore[typeddict-item]
    if "CampaignsResponse" in data:
        import aws_sdk_pinpoint.types.campaigns_response

        out["campaigns_response"] = (
            aws_sdk_pinpoint.types.campaigns_response.deserialize_json(
                data["CampaignsResponse"]
            )
        )
    return out
