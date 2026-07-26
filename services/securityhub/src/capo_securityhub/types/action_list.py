"""Generated from Smithy shape ``com.amazonaws.securityhub#ActionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action

ActionList: TypeAlias = list[
    "capo_securityhub.types.automation_rules_action.AutomationRulesAction"
]


# --- restJson1 ser/de ---
def serialize_json(value: ActionList) -> list:
    import capo_securityhub.types.automation_rules_action

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.automation_rules_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> ActionList:
    import capo_securityhub.types.automation_rules_action

    out: ActionList = []
    for item in data:
        out.append(
            capo_securityhub.types.automation_rules_action.deserialize_json(item)
        )
    return out
