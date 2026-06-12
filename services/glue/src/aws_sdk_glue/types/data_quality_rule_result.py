"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityRuleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_rule_result_description
    import aws_sdk_glue.types.data_quality_rule_result_status
    import aws_sdk_glue.types.evaluated_metrics_map
    import aws_sdk_glue.types.labels
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.rule_metrics_map


class DataQualityRuleResult(TypedDict):
    name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the data quality rule.</p>"""
    description: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>A description of the data quality rule.</p>"""
    evaluation_message: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>An evaluation message.</p>"""
    result: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_status.DataQualityRuleResultStatus"
    ]
    """<p>A pass or fail status for the rule.</p>"""
    evaluated_metrics: NotRequired[
        "aws_sdk_glue.types.evaluated_metrics_map.EvaluatedMetricsMap"
    ]
    """<p>A map of metrics associated with the evaluation of the rule.</p>"""
    evaluated_rule: NotRequired[
        "aws_sdk_glue.types.data_quality_rule_result_description.DataQualityRuleResultDescription"
    ]
    """<p>The evaluated rule.</p>"""
    rule_metrics: NotRequired["aws_sdk_glue.types.rule_metrics_map.RuleMetricsMap"]
    """<p>A map containing metrics associated with the evaluation of the rule based on row-level results. </p>"""
    labels: NotRequired["aws_sdk_glue.types.labels.Labels"]
    """<p>A map containing labels assigned to the data quality rule. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityRuleResult) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "evaluation_message" in value:
        out["EvaluationMessage"] = value["evaluation_message"]
    if "result" in value:
        import aws_sdk_glue.types.data_quality_rule_result_status

        out["Result"] = (
            aws_sdk_glue.types.data_quality_rule_result_status.serialize_aws_json_1_1(
                value["result"]
            )
        )
    if "evaluated_metrics" in value:
        import aws_sdk_glue.types.evaluated_metrics_map

        out["EvaluatedMetrics"] = (
            aws_sdk_glue.types.evaluated_metrics_map.serialize_aws_json_1_1(
                value["evaluated_metrics"]
            )
        )
    if "evaluated_rule" in value:
        out["EvaluatedRule"] = value["evaluated_rule"]
    if "rule_metrics" in value:
        import aws_sdk_glue.types.rule_metrics_map

        out["RuleMetrics"] = aws_sdk_glue.types.rule_metrics_map.serialize_aws_json_1_1(
            value["rule_metrics"]
        )
    if "labels" in value:
        import aws_sdk_glue.types.labels

        out["Labels"] = aws_sdk_glue.types.labels.serialize_aws_json_1_1(
            value["labels"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityRuleResult:
    out: DataQualityRuleResult = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EvaluationMessage" in data:
        out["evaluation_message"] = data["EvaluationMessage"]
    if "Result" in data:
        import aws_sdk_glue.types.data_quality_rule_result_status

        out["result"] = (
            aws_sdk_glue.types.data_quality_rule_result_status.deserialize_aws_json_1_1(
                data["Result"]
            )
        )
    if "EvaluatedMetrics" in data:
        import aws_sdk_glue.types.evaluated_metrics_map

        out["evaluated_metrics"] = (
            aws_sdk_glue.types.evaluated_metrics_map.deserialize_aws_json_1_1(
                data["EvaluatedMetrics"]
            )
        )
    if "EvaluatedRule" in data:
        out["evaluated_rule"] = data["EvaluatedRule"]
    if "RuleMetrics" in data:
        import aws_sdk_glue.types.rule_metrics_map

        out["rule_metrics"] = (
            aws_sdk_glue.types.rule_metrics_map.deserialize_aws_json_1_1(
                data["RuleMetrics"]
            )
        )
    if "Labels" in data:
        import aws_sdk_glue.types.labels

        out["labels"] = aws_sdk_glue.types.labels.deserialize_aws_json_1_1(
            data["Labels"]
        )
    return out
