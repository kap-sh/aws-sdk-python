"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityAnalyzerResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_rule_result_description
    import aws_sdk_glue.types.evaluated_metrics_map
    import aws_sdk_glue.types.name_string


class DataQualityAnalyzerResult(TypedDict, closed=True):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the data quality analyzer.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>A description of the data quality analyzer.</p>"""
    evaluation_message: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>An evaluation message.</p>"""
    evaluated_metrics: NotRequired[
        "aws_sdk_glue.types.evaluated_metrics_map.EvaluatedMetricsMap"
    ]
    """<p>A map of metrics associated with the evaluation of the analyzer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityAnalyzerResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "evaluation_message" in value:
        out["EvaluationMessage"] = value["evaluation_message"]
    if "evaluated_metrics" in value:
        import aws_sdk_glue.types.evaluated_metrics_map

        out["EvaluatedMetrics"] = (
            aws_sdk_glue.types.evaluated_metrics_map.serialize_aws_json_1_1(
                value["evaluated_metrics"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityAnalyzerResult:
    out: DataQualityAnalyzerResult = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EvaluationMessage" in data:
        out["evaluation_message"] = data["EvaluationMessage"]
    if "EvaluatedMetrics" in data:
        import aws_sdk_glue.types.evaluated_metrics_map

        out["evaluated_metrics"] = (
            aws_sdk_glue.types.evaluated_metrics_map.deserialize_aws_json_1_1(
                data["EvaluatedMetrics"]
            )
        )
    return out
