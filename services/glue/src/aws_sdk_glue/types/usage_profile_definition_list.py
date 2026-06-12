"""Generated from Smithy shape ``com.amazonaws.glue#UsageProfileDefinitionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.usage_profile_definition

UsageProfileDefinitionList: TypeAlias = list[
    "aws_sdk_glue.types.usage_profile_definition.UsageProfileDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsageProfileDefinitionList) -> list:
    import aws_sdk_glue.types.usage_profile_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.usage_profile_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsageProfileDefinitionList:
    import aws_sdk_glue.types.usage_profile_definition

    out: UsageProfileDefinitionList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.usage_profile_definition.deserialize_aws_json_1_1(item)
        )
    return out
