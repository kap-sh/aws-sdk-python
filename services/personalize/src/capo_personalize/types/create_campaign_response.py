"""Generated from Smithy shape ``com.amazonaws.personalize#CreateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn


class CreateCampaignResponse(TypedDict, closed=True):
    campaign_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCampaignResponse) -> dict:
    out: dict = {}
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCampaignResponse:
    out: CreateCampaignResponse = {}  # type: ignore[typeddict-item]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    return out
