"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.campaign_arn
    import aws_sdk_iotfleetwise.types.campaign_name


class CreateCampaignResponse(TypedDict, closed=True):
    name: NotRequired["aws_sdk_iotfleetwise.types.campaign_name.campaignName"]
    """<p>The name of the created campaign.</p>"""
    arn: NotRequired["aws_sdk_iotfleetwise.types.campaign_arn.campaignArn"]
    """<p> The ARN of the created campaign. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateCampaignResponse) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateCampaignResponse:
    out: CreateCampaignResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "arn" in data:
        out["arn"] = data["arn"]
    return out
