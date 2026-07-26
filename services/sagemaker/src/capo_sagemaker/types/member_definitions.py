"""Generated from Smithy shape ``com.amazonaws.sagemaker#MemberDefinitions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.member_definition

MemberDefinitions: TypeAlias = list[
    "capo_sagemaker.types.member_definition.MemberDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MemberDefinitions) -> list:
    import capo_sagemaker.types.member_definition

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.member_definition.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> MemberDefinitions:
    import capo_sagemaker.types.member_definition

    out: MemberDefinitions = []
    for item in data:
        out.append(
            capo_sagemaker.types.member_definition.deserialize_aws_json_1_1(item)
        )
    return out
