"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListAnomaliesRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.anomaly_detector_arn
    import aws_sdk_cloudwatch_logs.types.list_anomalies_limit
    import aws_sdk_cloudwatch_logs.types.next_token
    import aws_sdk_cloudwatch_logs.types.suppression_state


class ListAnomaliesRequest(TypedDict):
    anomaly_detector_arn: NotRequired[
        "aws_sdk_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    ]
    """<p>Use this to optionally limit the results to only the anomalies found by a certain anomaly detector.</p>"""
    suppression_state: NotRequired[
        "aws_sdk_cloudwatch_logs.types.suppression_state.SuppressionState"
    ]
    """<p>You can specify this parameter if you want to the operation to return only anomalies that are currently either suppressed or unsuppressed.</p>"""
    limit: NotRequired[
        "aws_sdk_cloudwatch_logs.types.list_anomalies_limit.ListAnomaliesLimit"
    ]
    """<p>The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAnomaliesRequest) -> dict:
    out: dict = {}
    if "anomaly_detector_arn" in value:
        out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    if "suppression_state" in value:
        import aws_sdk_cloudwatch_logs.types.suppression_state

        out["suppressionState"] = (
            aws_sdk_cloudwatch_logs.types.suppression_state.serialize_aws_json_1_1(
                value["suppression_state"]
            )
        )
    if "limit" in value:
        out["limit"] = value["limit"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAnomaliesRequest:
    out: ListAnomaliesRequest = {}  # type: ignore[typeddict-item]
    if "anomalyDetectorArn" in data:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    if "suppressionState" in data:
        import aws_sdk_cloudwatch_logs.types.suppression_state

        out["suppression_state"] = (
            aws_sdk_cloudwatch_logs.types.suppression_state.deserialize_aws_json_1_1(
                data["suppressionState"]
            )
        )
    if "limit" in data:
        out["limit"] = data["limit"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
