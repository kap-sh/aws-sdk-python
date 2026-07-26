"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#CreateLogAnomalyDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detector_arn


class CreateLogAnomalyDetectorResponse(TypedDict, closed=True):
    anomaly_detector_arn: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
    ]
    """<p>The ARN of the log anomaly detector that you just created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLogAnomalyDetectorResponse) -> dict:
    out: dict = {}
    if "anomaly_detector_arn" in value:
        out["anomalyDetectorArn"] = value["anomaly_detector_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLogAnomalyDetectorResponse:
    out: CreateLogAnomalyDetectorResponse = {}  # type: ignore[typeddict-item]
    if "anomalyDetectorArn" in data:
        out["anomaly_detector_arn"] = data["anomalyDetectorArn"]
    return out
