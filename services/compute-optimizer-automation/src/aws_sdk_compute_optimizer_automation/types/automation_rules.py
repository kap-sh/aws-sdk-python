"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#AutomationRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_rule

AutomationRules: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.automation_rule.AutomationRule"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AutomationRules) -> list:
    import aws_sdk_compute_optimizer_automation.types.automation_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.automation_rule.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> AutomationRules:
    import aws_sdk_compute_optimizer_automation.types.automation_rule

    out: AutomationRules = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.automation_rule.deserialize_aws_json_1_0(
                item
            )
        )
    return out
