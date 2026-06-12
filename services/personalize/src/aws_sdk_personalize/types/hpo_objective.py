"""Generated from Smithy shape ``com.amazonaws.personalize#HPOObjective``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.hpo_objective_type
    import aws_sdk_personalize.types.metric_name
    import aws_sdk_personalize.types.metric_regex


class HPOObjective(TypedDict):
    type: NotRequired["aws_sdk_personalize.types.hpo_objective_type.HPOObjectiveType"]
    """<p>The type of the metric. Valid values are <code>Maximize</code> and <code>Minimize</code>.</p>"""
    metric_name: NotRequired["aws_sdk_personalize.types.metric_name.MetricName"]
    """<p>The name of the metric.</p>"""
    metric_regex: NotRequired["aws_sdk_personalize.types.metric_regex.MetricRegex"]
    """<p>A regular expression for finding the metric in the training job logs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HPOObjective) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "metric_name" in value:
        out["metricName"] = value["metric_name"]
    if "metric_regex" in value:
        out["metricRegex"] = value["metric_regex"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HPOObjective:
    out: HPOObjective = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "metricName" in data:
        out["metric_name"] = data["metricName"]
    if "metricRegex" in data:
        out["metric_regex"] = data["metricRegex"]
    return out
