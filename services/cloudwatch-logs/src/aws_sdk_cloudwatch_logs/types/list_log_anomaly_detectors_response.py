"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogAnomalyDetectorsResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.anomaly_detectors
    import aws_sdk_cloudwatch_logs.types.next_token


class ListLogAnomalyDetectorsResponse(TypedDict):
    anomaly_detectors: NotRequired[
        "aws_sdk_cloudwatch_logs.types.anomaly_detectors.AnomalyDetectors"
    ]
    """<p>An array of structures, where each structure in the array contains information about one anomaly detector.</p>"""
    next_token: NotRequired["aws_sdk_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogAnomalyDetectorsResponse) -> dict:
    out: dict = {}
    if "anomaly_detectors" in value:
        import aws_sdk_cloudwatch_logs.types.anomaly_detectors

        out["anomalyDetectors"] = (
            aws_sdk_cloudwatch_logs.types.anomaly_detectors.serialize_aws_json_1_1(
                value["anomaly_detectors"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogAnomalyDetectorsResponse:
    out: ListLogAnomalyDetectorsResponse = {}  # type: ignore[typeddict-item]
    if "anomalyDetectors" in data:
        import aws_sdk_cloudwatch_logs.types.anomaly_detectors

        out["anomaly_detectors"] = (
            aws_sdk_cloudwatch_logs.types.anomaly_detectors.deserialize_aws_json_1_1(
                data["anomalyDetectors"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
