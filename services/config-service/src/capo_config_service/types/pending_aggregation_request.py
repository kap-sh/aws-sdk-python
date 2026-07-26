"""Generated from Smithy shape ``com.amazonaws.configservice#PendingAggregationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_id
    import capo_config_service.types.aws_region


class PendingAggregationRequest(TypedDict, closed=True):
    requester_account_id: NotRequired["capo_config_service.types.account_id.AccountId"]
    """<p>The 12-digit account ID of the account requesting to aggregate data.</p>"""
    requester_aws_region: NotRequired["capo_config_service.types.aws_region.AwsRegion"]
    """<p>The region requesting to aggregate data. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingAggregationRequest) -> dict:
    out: dict = {}
    if "requester_account_id" in value:
        out["RequesterAccountId"] = value["requester_account_id"]
    if "requester_aws_region" in value:
        out["RequesterAwsRegion"] = value["requester_aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingAggregationRequest:
    out: PendingAggregationRequest = {}  # type: ignore[typeddict-item]
    if "RequesterAccountId" in data:
        out["requester_account_id"] = data["RequesterAccountId"]
    if "RequesterAwsRegion" in data:
        out["requester_aws_region"] = data["RequesterAwsRegion"]
    return out
