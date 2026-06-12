"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProfilerRuleConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.profiler_rule_configuration

ProfilerRuleConfigurations: TypeAlias = list[
    "aws_sdk_sagemaker.types.profiler_rule_configuration.ProfilerRuleConfiguration"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProfilerRuleConfigurations) -> list:
    import aws_sdk_sagemaker.types.profiler_rule_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.profiler_rule_configuration.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProfilerRuleConfigurations:
    import aws_sdk_sagemaker.types.profiler_rule_configuration

    out: ProfilerRuleConfigurations = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.profiler_rule_configuration.deserialize_aws_json_1_1(
                item
            )
        )
    return out
