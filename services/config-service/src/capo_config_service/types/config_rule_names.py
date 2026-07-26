"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigRuleNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name

ConfigRuleNames: TypeAlias = list[
    "capo_config_service.types.config_rule_name.ConfigRuleName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfigRuleNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConfigRuleNames:
    return list(data)
