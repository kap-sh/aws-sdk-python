"""Generated from Smithy shape ``com.amazonaws.configservice#ReevaluateConfigRuleNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.config_rule_name

ReevaluateConfigRuleNames: TypeAlias = list[
    "capo_config_service.types.config_rule_name.ConfigRuleName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReevaluateConfigRuleNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ReevaluateConfigRuleNames:
    return list(data)
