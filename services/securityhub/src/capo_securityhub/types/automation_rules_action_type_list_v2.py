"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionTypeListV2``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_action_type_object_v2

AutomationRulesActionTypeListV2: TypeAlias = list[
    "capo_securityhub.types.automation_rules_action_type_object_v2.AutomationRulesActionTypeObjectV2"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionTypeListV2) -> list:
    import capo_securityhub.types.automation_rules_action_type_object_v2

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.automation_rules_action_type_object_v2.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AutomationRulesActionTypeListV2:
    import capo_securityhub.types.automation_rules_action_type_object_v2

    out: AutomationRulesActionTypeListV2 = []
    for item in data:
        out.append(
            capo_securityhub.types.automation_rules_action_type_object_v2.deserialize_json(
                item
            )
        )
    return out
