"""Generated from Smithy shape ``com.amazonaws.sagemaker#MetricDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.metric_name
    import aws_sdk_sagemaker.types.metric_regex


class MetricDefinition(TypedDict):
    name: NotRequired["aws_sdk_sagemaker.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    regex: NotRequired["aws_sdk_sagemaker.types.metric_regex.MetricRegex"]
    """<p>A regular expression that searches the output of a training job and gets the value of the metric. For more information about using regular expressions to define metrics, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-define-metrics-variables.html\">Defining metrics and environment variables</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricDefinition) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "regex" in value:
        out["Regex"] = value["regex"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricDefinition:
    out: MetricDefinition = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Regex" in data:
        out["regex"] = data["Regex"]
    return out
