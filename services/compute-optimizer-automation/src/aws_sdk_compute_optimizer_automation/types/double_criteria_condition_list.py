"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#DoubleCriteriaConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.double_criteria_condition

DoubleCriteriaConditionList: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.double_criteria_condition.DoubleCriteriaCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DoubleCriteriaConditionList) -> list:
    import aws_sdk_compute_optimizer_automation.types.double_criteria_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.double_criteria_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DoubleCriteriaConditionList:
    import aws_sdk_compute_optimizer_automation.types.double_criteria_condition

    out: DoubleCriteriaConditionList = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.double_criteria_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
