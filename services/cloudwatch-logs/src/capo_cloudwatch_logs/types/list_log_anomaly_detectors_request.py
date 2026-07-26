"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogAnomalyDetectorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.list_log_anomaly_detectors_limit
    import capo_cloudwatch_logs.types.log_group_arn
    import capo_cloudwatch_logs.types.next_token


class ListLogAnomalyDetectorsRequest(TypedDict, closed=True):
    filter_log_group_arn: NotRequired[
        "capo_cloudwatch_logs.types.log_group_arn.LogGroupArn"
    ]
    """<p>Use this to optionally filter the results to only include anomaly detectors that are associated with the specified log group.</p>"""
    limit: NotRequired[
        "capo_cloudwatch_logs.types.list_log_anomaly_detectors_limit.ListLogAnomalyDetectorsLimit"
    ]
    """<p>The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogAnomalyDetectorsRequest) -> dict:
    out: dict = {}
    if "filter_log_group_arn" in value:
        out["filterLogGroupArn"] = value["filter_log_group_arn"]
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogAnomalyDetectorsRequest:
    out: ListLogAnomalyDetectorsRequest = {}  # type: ignore[typeddict-item]
    if "filterLogGroupArn" in data:
        out["filter_log_group_arn"] = data["filterLogGroupArn"]
    if "limit" in data:
        out["limit"] = data["limit"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
