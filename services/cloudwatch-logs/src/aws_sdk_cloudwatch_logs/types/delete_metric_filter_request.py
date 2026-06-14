"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#DeleteMetricFilterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.filter_name
    import aws_sdk_cloudwatch_logs.types.log_group_name


class DeleteMetricFilterRequest(TypedDict):
    log_group_name: "aws_sdk_cloudwatch_logs.types.log_group_name.LogGroupName"
    """<p>The name of the log group.</p>"""
    filter_name: "aws_sdk_cloudwatch_logs.types.filter_name.FilterName"
    """<p>The name of the metric filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMetricFilterRequest) -> dict:
    out: dict = {}
    out["logGroupName"] = value["log_group_name"]
    out["filterName"] = value["filter_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMetricFilterRequest:
    out: DeleteMetricFilterRequest = {}  # type: ignore[typeddict-item]
    if "logGroupName" in data:
        out["log_group_name"] = data["logGroupName"]
    else:
        raise DeserializationError("DeleteMetricFilterRequest.log_group_name required")
    if "filterName" in data:
        out["filter_name"] = data["filterName"]
    else:
        raise DeserializationError("DeleteMetricFilterRequest.filter_name required")
    return out
