"""Generated from Smithy shape ``com.amazonaws.personalize#DescribeCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import capo_personalize.types.arn


class DescribeCampaignRequest(TypedDict, closed=True):
    campaign_arn: "capo_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the campaign.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeCampaignRequest) -> dict:
    out: dict = {}
    out["campaignArn"] = value["campaign_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeCampaignRequest:
    out: DescribeCampaignRequest = {}  # type: ignore[typeddict-item]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    else:
        raise DeserializationError("DescribeCampaignRequest.campaign_arn required")
    return out
