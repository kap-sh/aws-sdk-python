"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.float
    import capo_sagemaker.types.metric_name
    import capo_sagemaker.types.timestamp


class MetricData(TypedDict, closed=True):
    metric_name: NotRequired["capo_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    value: NotRequired["capo_sagemaker.types.float.Float"]
    """<p>The value of the metric.</p>"""
    timestamp: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The date and time that the algorithm emitted the metric.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricData) -> dict:
    out: dict = {}
    if "metric_name" in value:
        out["MetricName"] = value["metric_name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "timestamp" in value:
        import capo_sagemaker.types.timestamp

        out["Timestamp"] = capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
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
        import capo_sagemaker.types.timestamp

        out["timestamp"] = capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    return out
