"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigRulesFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.evaluation_mode
    import capo_config_service.types.rule_evaluation_visibility


class DescribeConfigRulesFilters(TypedDict, closed=True):
    evaluation_mode: NotRequired[
        "capo_config_service.types.evaluation_mode.EvaluationMode"
    ]
    """<p>The mode of an evaluation. The valid values are Detective or Proactive.</p>"""
    rule_evaluation_visibility: NotRequired[
        "capo_config_service.types.rule_evaluation_visibility.RuleEvaluationVisibility"
    ]
    """<p>Filters the results by <code>RuleEvaluationVisibility</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigRulesFilters) -> dict:
    out: dict = {}
    if "evaluation_mode" in value:
        import capo_config_service.types.evaluation_mode

        out["EvaluationMode"] = (
            capo_config_service.types.evaluation_mode.serialize_aws_json_1_1(
                value["evaluation_mode"]
            )
        )
    if "rule_evaluation_visibility" in value:
        import capo_config_service.types.rule_evaluation_visibility

        out["RuleEvaluationVisibility"] = (
            capo_config_service.types.rule_evaluation_visibility.serialize_aws_json_1_1(
                value["rule_evaluation_visibility"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigRulesFilters:
    out: DescribeConfigRulesFilters = {}  # type: ignore[typeddict-item]
    if "EvaluationMode" in data:
        import capo_config_service.types.evaluation_mode

        out["evaluation_mode"] = (
            capo_config_service.types.evaluation_mode.deserialize_aws_json_1_1(
                data["EvaluationMode"]
            )
        )
    if "RuleEvaluationVisibility" in data:
        import capo_config_service.types.rule_evaluation_visibility

        out["rule_evaluation_visibility"] = (
            capo_config_service.types.rule_evaluation_visibility.deserialize_aws_json_1_1(
                data["RuleEvaluationVisibility"]
            )
        )
    return out
