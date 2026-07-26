"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.automation_rules_config

AutomationRulesConfigList: TypeAlias = list[
    "capo_securityhub.types.automation_rules_config.AutomationRulesConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesConfigList) -> list:
    import capo_securityhub.types.automation_rules_config

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.automation_rules_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> AutomationRulesConfigList:
    import capo_securityhub.types.automation_rules_config

    out: AutomationRulesConfigList = []
    for item in data:
        out.append(
            capo_securityhub.types.automation_rules_config.deserialize_json(item)
        )
    return out
