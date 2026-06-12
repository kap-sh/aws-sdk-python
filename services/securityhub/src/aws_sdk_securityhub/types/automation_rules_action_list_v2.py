"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionListV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_v2

AutomationRulesActionListV2: TypeAlias = list[
    "aws_sdk_securityhub.types.automation_rules_action_v2.AutomationRulesActionV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionListV2) -> list:
    import aws_sdk_securityhub.types.automation_rules_action_v2

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.automation_rules_action_v2.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomationRulesActionListV2:
    import aws_sdk_securityhub.types.automation_rules_action_v2

    out: AutomationRulesActionListV2 = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.automation_rules_action_v2.deserialize_json(item)
        )
    return out
