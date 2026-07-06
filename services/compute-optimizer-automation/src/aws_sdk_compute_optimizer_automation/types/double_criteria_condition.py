"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DoubleCriteriaCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.comparison_operator
    import aws_sdk_compute_optimizer_automation.types.double_list


class DoubleCriteriaCondition(TypedDict, closed=True):
    comparison: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.comparison_operator.ComparisonOperator"
    ]
    """<p>The comparison operator to use, such as equals, greater than, less than, etc.</p>"""
    values: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.double_list.DoubleList"
    ]
    """<p>The list of double values to compare against using the specified comparison operator.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DoubleCriteriaCondition) -> dict:
    out: dict = {}
    if "comparison" in value:
        import aws_sdk_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            aws_sdk_compute_optimizer_automation.types.comparison_operator.serialize_aws_json_1_0(
                value["comparison"]
            )
        )
    if "values" in value:
        import aws_sdk_compute_optimizer_automation.types.double_list

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.double_list.serialize_aws_json_1_0(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DoubleCriteriaCondition:
    out: DoubleCriteriaCondition = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_compute_optimizer_automation.types.comparison_operator

        out["comparison"] = (
            aws_sdk_compute_optimizer_automation.types.comparison_operator.deserialize_aws_json_1_0(
                data["comparison"]
            )
        )
    if "values" in data:
        import aws_sdk_compute_optimizer_automation.types.double_list

        out["values"] = (
            aws_sdk_compute_optimizer_automation.types.double_list.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    return out
