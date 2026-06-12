"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_config

AutomationRulesConfigList: TypeAlias = list[
    "aws_sdk_securityhub.types.automation_rules_config.AutomationRulesConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesConfigList) -> list:
    import aws_sdk_securityhub.types.automation_rules_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.automation_rules_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomationRulesConfigList:
    import aws_sdk_securityhub.types.automation_rules_config

    out: AutomationRulesConfigList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.automation_rules_config.deserialize_json(item)
        )
    return out
