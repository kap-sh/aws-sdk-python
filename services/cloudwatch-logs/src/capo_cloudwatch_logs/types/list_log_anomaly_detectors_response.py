"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ListLogAnomalyDetectorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.anomaly_detectors
    import capo_cloudwatch_logs.types.next_token


class ListLogAnomalyDetectorsResponse(TypedDict, closed=True):
    anomaly_detectors: NotRequired[
        "capo_cloudwatch_logs.types.anomaly_detectors.AnomalyDetectors"
    ]
    """<p>An array of structures, where each structure in the array contains information about one anomaly detector.</p>"""
    next_token: NotRequired["capo_cloudwatch_logs.types.next_token.NextToken"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLogAnomalyDetectorsResponse) -> dict:
    out: dict = {}
    if "anomaly_detectors" in value:
        import capo_cloudwatch_logs.types.anomaly_detectors

        out["anomalyDetectors"] = (
            capo_cloudwatch_logs.types.anomaly_detectors.serialize_aws_json_1_1(
                value["anomaly_detectors"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLogAnomalyDetectorsResponse:
    out: ListLogAnomalyDetectorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("anomalyDetectors") is not None:
        import capo_cloudwatch_logs.types.anomaly_detectors

        out["anomaly_detectors"] = (
            capo_cloudwatch_logs.types.anomaly_detectors.deserialize_aws_json_1_1(
                data["anomalyDetectors"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
