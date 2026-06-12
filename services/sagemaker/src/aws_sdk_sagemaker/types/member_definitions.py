"""Generated from Smithy shape ``com.amazonaws.sagemaker#MemberDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.member_definition

MemberDefinitions: TypeAlias = list[
    "aws_sdk_sagemaker.types.member_definition.MemberDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberDefinitions) -> list:
    import aws_sdk_sagemaker.types.member_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.member_definition.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MemberDefinitions:
    import aws_sdk_sagemaker.types.member_definition

    out: MemberDefinitions = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.member_definition.deserialize_aws_json_1_1(item)
        )
    return out
