"""Generated from Smithy shape ``com.amazonaws.personalize#UpdateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class UpdateCampaignResponse(TypedDict, closed=True):
    campaign_arn: NotRequired["aws_sdk_personalize.types.arn.Arn"]
    """<p>The same campaign ARN as given in the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCampaignResponse) -> dict:
    out: dict = {}
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCampaignResponse:
    out: UpdateCampaignResponse = {}  # type: ignore[typeddict-item]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    return out
