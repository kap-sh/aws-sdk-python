"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ResourceTagsCriteriaCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.comparison_operator
    import capo_compute_optimizer_automation.types.string_criteria_value
    import capo_compute_optimizer_automation.types.string_criteria_values


class ResourceTagsCriteriaCondition(TypedDict, closed=True):
    comparison: NotRequired[
        "capo_compute_optimizer_automation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator used to evaluate the tag criteria, such as equals, not equals, or contains.</p>"""
    key: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_value.StringCriteriaValue"
    ]
    """<p>The tag key to use for comparison when filtering resources.</p>"""
    values: NotRequired[
        "capo_compute_optimizer_automation.types.string_criteria_values.StringCriteriaValues"
    ]
    """<p>List of tag values to compare against when filtering resources.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTagsCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison"]
            )
        )
    if "key" in value:
        out["key"] = value["key"]
    if "values" in value:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceTagsCriteriaCondition:
    out: ResourceTagsCriteriaCondition = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import capo_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            capo_compute_optimizer_automation.types.comparison_operator.deserialize_aws_json_1_0(
                data["comparison"]
            )
        )
    if "key" in data:
        out["key"] = data["key"]
    if "values" in data:
        import capo_compute_optimizer_automation.types.string_criteria_values

        out["values"] = (
            capo_compute_optimizer_automation.types.string_criteria_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
