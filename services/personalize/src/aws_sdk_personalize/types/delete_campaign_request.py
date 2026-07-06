"""Generated from Smithy shape ``com.amazonaws.personalize#DeleteCampaignRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_personalize.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_personalize.types.arn


class DeleteCampaignRequest(TypedDict, closed=True):
    campaign_arn: "aws_sdk_personalize.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the campaign to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteCampaignRequest) -> dict:
    out: dict = {}
    out["campaignArn"] = value["campaign_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteCampaignRequest:
    out: DeleteCampaignRequest = {}  # type: ignore[typeddict-item]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    else:
        raise DeserializationError("DeleteCampaignRequest.campaign_arn required")
    return out
