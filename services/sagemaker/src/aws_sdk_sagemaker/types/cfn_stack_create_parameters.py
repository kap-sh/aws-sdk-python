"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnStackCreateParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_stack_create_parameter

CfnStackCreateParameters: TypeAlias = list[
    "aws_sdk_sagemaker.types.cfn_stack_create_parameter.CfnStackCreateParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnStackCreateParameters) -> list:
    import aws_sdk_sagemaker.types.cfn_stack_create_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cfn_stack_create_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CfnStackCreateParameters:
    import aws_sdk_sagemaker.types.cfn_stack_create_parameter

    out: CfnStackCreateParameters = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cfn_stack_create_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
