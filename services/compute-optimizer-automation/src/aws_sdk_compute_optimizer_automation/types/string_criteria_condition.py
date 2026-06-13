"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#StringCriteriaCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.comparison_operator
    import aws_sdk_compute_optimizer_automation.types.string_criteria_values


class StringCriteriaCondition(TypedDict):
    comparison: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator used to evaluate the string criteria, such as equals, not equals, or contains.</p>"""
    values: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.string_criteria_values.StringCriteriaValues"
    ]
    """<p>List of string values to compare against when applying the criteria condition.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StringCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import aws_sdk_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            aws_sdk_compute_optimizer_automation.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison"]
            )
        )
    if "values" in value:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StringCriteriaCondition:
    out: StringCriteriaCondition = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            aws_sdk_compute_optimizer_automation.types.comparison_operator.deserialize_aws_json_1_0(
                data["comparison"]
            )
        )
    if "values" in data:
        import aws_sdk_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.string_criteria_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
