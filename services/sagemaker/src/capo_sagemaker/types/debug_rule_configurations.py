"""Generated from Smithy shape ``com.amazonaws.sagemaker#DebugRuleConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.debug_rule_configuration

DebugRuleConfigurations: TypeAlias = list[
    "capo_sagemaker.types.debug_rule_configuration.DebugRuleConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DebugRuleConfigurations) -> list:
    import capo_sagemaker.types.debug_rule_configuration

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.debug_rule_configuration.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DebugRuleConfigurations:
    import capo_sagemaker.types.debug_rule_configuration

    out: DebugRuleConfigurations = []
    for item in data:
        out.append(
            capo_sagemaker.types.debug_rule_configuration.deserialize_aws_json_1_1(item)
        )
    return out
