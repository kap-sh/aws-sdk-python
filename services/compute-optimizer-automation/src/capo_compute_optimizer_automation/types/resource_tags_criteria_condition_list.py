"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ResourceTagsCriteriaConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.resource_tags_criteria_condition

ResourceTagsCriteriaConditionList: TypeAlias = list[
    "capo_compute_optimizer_automation.types.resource_tags_criteria_condition.ResourceTagsCriteriaCondition"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceTagsCriteriaConditionList) -> list:
    import capo_compute_optimizer_automation.types.resource_tags_criteria_condition

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ResourceTagsCriteriaConditionList:
    import capo_compute_optimizer_automation.types.resource_tags_criteria_condition

    out: ResourceTagsCriteriaConditionList = []
    for item in data:
        out.append(
            capo_compute_optimizer_automation.types.resource_tags_criteria_condition.deserialize_aws_json_1_0(
                item
            )
        )
    return out
