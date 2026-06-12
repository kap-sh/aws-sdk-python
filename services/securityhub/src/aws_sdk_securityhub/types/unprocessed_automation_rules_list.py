"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedAutomationRulesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.unprocessed_automation_rule

UnprocessedAutomationRulesList: TypeAlias = list[
    "aws_sdk_securityhub.types.unprocessed_automation_rule.UnprocessedAutomationRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedAutomationRulesList) -> list:
    import aws_sdk_securityhub.types.unprocessed_automation_rule

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.unprocessed_automation_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UnprocessedAutomationRulesList:
    import aws_sdk_securityhub.types.unprocessed_automation_rule

    out: UnprocessedAutomationRulesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.unprocessed_automation_rule.deserialize_json(item)
        )
    return out
