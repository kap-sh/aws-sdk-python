"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationPropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_configuration_property

RuleConfigurationPropertyList: TypeAlias = list[
    "aws_sdk_codepipeline.types.rule_configuration_property.RuleConfigurationProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleConfigurationPropertyList) -> list:
    import aws_sdk_codepipeline.types.rule_configuration_property

    out: list = []
    for item in value:
        out.append(
            aws_sdk_codepipeline.types.rule_configuration_property.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> RuleConfigurationPropertyList:
    import aws_sdk_codepipeline.types.rule_configuration_property

    out: RuleConfigurationPropertyList = []
    for item in data:
        out.append(
            aws_sdk_codepipeline.types.rule_configuration_property.deserialize_aws_json_1_1(
                item
            )
        )
    return out
