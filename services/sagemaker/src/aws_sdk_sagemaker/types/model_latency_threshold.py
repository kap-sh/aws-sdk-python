"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelLatencyThreshold``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.integer
    import aws_sdk_sagemaker.types.string64


class ModelLatencyThreshold(TypedDict):
    percentile: NotRequired["aws_sdk_sagemaker.types.string64.String64"]
    """<p>The model latency percentile threshold. Acceptable values are <code>P95</code> and <code>P99</code>. For custom load tests, specify the value as <code>P95</code>.</p>"""
    value_in_milliseconds: NotRequired["aws_sdk_sagemaker.types.integer.Integer"]
    """<p>The model latency percentile value in milliseconds.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelLatencyThreshold) -> dict:
    out: dict = {}
    if "percentile" in value:
        out["Percentile"] = value["percentile"]
    if "value_in_milliseconds" in value:
        out["ValueInMilliseconds"] = value["value_in_milliseconds"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelLatencyThreshold:
    out: ModelLatencyThreshold = {}  # type: ignore[typeddict-item]
    if "Percentile" in data:
        out["percentile"] = data["Percentile"]
    if "ValueInMilliseconds" in data:
        out["value_in_milliseconds"] = data["ValueInMilliseconds"]
    return out
