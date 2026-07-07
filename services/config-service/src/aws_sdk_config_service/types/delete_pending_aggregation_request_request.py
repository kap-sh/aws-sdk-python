"""Generated from Smithy shape ``com.amazonaws.configservice#DeletePendingAggregationRequestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_config_service.types.account_id
    import aws_sdk_config_service.types.aws_region


class DeletePendingAggregationRequestRequest(TypedDict, closed=True):
    requester_account_id: "aws_sdk_config_service.types.account_id.AccountId"
    """<p>The 12-digit account ID of the account requesting to aggregate data.</p>"""
    requester_aws_region: "aws_sdk_config_service.types.aws_region.AwsRegion"
    """<p>The region requesting to aggregate data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletePendingAggregationRequestRequest) -> dict:
    out: dict = {}
    out["RequesterAccountId"] = value["requester_account_id"]
    out["RequesterAwsRegion"] = value["requester_aws_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeletePendingAggregationRequestRequest:
    out: DeletePendingAggregationRequestRequest = {}  # type: ignore[typeddict-item]
    if "RequesterAccountId" in data:
        out["requester_account_id"] = data["RequesterAccountId"]
    else:
        raise DeserializationError(
            "DeletePendingAggregationRequestRequest.requester_account_id required"
        )
    if "RequesterAwsRegion" in data:
        out["requester_aws_region"] = data["RequesterAwsRegion"]
    else:
        raise DeserializationError(
            "DeletePendingAggregationRequestRequest.requester_aws_region required"
        )
    return out
