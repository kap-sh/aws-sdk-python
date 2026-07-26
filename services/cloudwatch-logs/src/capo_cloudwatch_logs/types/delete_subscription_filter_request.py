"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteSubscriptionFilterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.log_group_name


class DeleteSubscriptionFilterRequest(TypedDict, closed=True):
    log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName"
    """<p>The name of the subscription filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSubscriptionFilterRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["filterName"] = value["filter_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSubscriptionFilterRequest:
    out: DeleteSubscriptionFilterRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError(
            "DeleteSubscriptionFilterRequest.log_group_name required"
        )
    if "filterName" in data:
        out["filter_name"] = data["filterName"]
    else:
        raise DeserializationError(
            "DeleteSubscriptionFilterRequest.filter_name required"
        )
    return out
