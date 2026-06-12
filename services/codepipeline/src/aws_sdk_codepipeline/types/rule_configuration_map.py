"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_configuration_key
    import aws_sdk_codepipeline.types.rule_configuration_value

RuleConfigurationMap: TypeAlias = dict[
    "aws_sdk_codepipeline.types.rule_configuration_key.RuleConfigurationKey",
    "aws_sdk_codepipeline.types.rule_configuration_value.RuleConfigurationValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RuleConfigurationMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleConfigurationMap:
    out: RuleConfigurationMap = {}
    for key, value in data.items():
        out[key] = value
    return out
