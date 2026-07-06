"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#FailedCampaignStateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.campaign_id
    import aws_sdk_connectcampaigns.types.get_campaign_state_batch_failure_code


class FailedCampaignStateResponse(TypedDict, closed=True):
    campaign_id: NotRequired["aws_sdk_connectcampaigns.types.campaign_id.CampaignId"]
    failure_code: NotRequired[
        "aws_sdk_connectcampaigns.types.get_campaign_state_batch_failure_code.GetCampaignStateBatchFailureCode"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: FailedCampaignStateResponse) -> dict:
    out: dict = {}
    if "campaign_id" in value:
        out["campaignId"] = value["campaign_id"]
    if "failure_code" in value:
        out["failureCode"] = value["failure_code"]
    return out


def deserialize_json(data: dict) -> FailedCampaignStateResponse:
    out: FailedCampaignStateResponse = {}  # type: ignore[typeddict-item]
    if "campaignId" in data:
        out["campaign_id"] = data["campaignId"]
    if "failureCode" in data:
        out["failure_code"] = data["failureCode"]
    return out
