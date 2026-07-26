"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetCampaignVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.campaign_response


class GetCampaignVersionResponse(TypedDict, closed=True):
    campaign_response: NotRequired[
        "capo_pinpoint.types.campaign_response.CampaignResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetCampaignVersionResponse) -> dict:
    out: dict = {}
    if "campaign_response" in value:
        import capo_pinpoint.types.campaign_response

        out["CampaignResponse"] = capo_pinpoint.types.campaign_response.serialize_json(
            value["campaign_response"]
        )
    return out


def deserialize_json(data: dict) -> GetCampaignVersionResponse:
    out: GetCampaignVersionResponse = {}  # type: ignore[typeddict-item]
    if "CampaignResponse" in data:
        import capo_pinpoint.types.campaign_response

        out["campaign_response"] = (
            capo_pinpoint.types.campaign_response.deserialize_json(
                data["CampaignResponse"]
            )
        )
    return out
