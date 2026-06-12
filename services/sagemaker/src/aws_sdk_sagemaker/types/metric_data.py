"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.float
    import aws_sdk_sagemaker.types.metric_name
    import aws_sdk_sagemaker.types.timestamp


class MetricData(TypedDict):
    metric_name: NotRequired["aws_sdk_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    value: NotRequired["aws_sdk_sagemaker.types.float.Float"]
    """<p>The value of the metric.</p>"""
    timestamp: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the algorithm emitted the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricData) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "timestamp" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["Timestamp"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricData:
    out: MetricData = {}  # type: ignore[typeddict-item]
    if "MetricName" in data:
        out["metric_name"] = data["MetricName"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Timestamp" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["timestamp"] = aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
