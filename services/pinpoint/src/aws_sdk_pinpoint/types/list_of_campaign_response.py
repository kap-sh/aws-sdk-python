"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfCampaignResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.campaign_response

ListOfCampaignResponse: TypeAlias = list[
    "aws_sdk_pinpoint.types.campaign_response.CampaignResponse"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfCampaignResponse) -> list:
    import aws_sdk_pinpoint.types.campaign_response

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.campaign_response.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfCampaignResponse:
    import aws_sdk_pinpoint.types.campaign_response

    out: ListOfCampaignResponse = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.campaign_response.deserialize_json(item))
    return out
