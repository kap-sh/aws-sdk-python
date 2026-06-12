"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnStackUpdateParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cfn_stack_update_parameter

CfnStackUpdateParameters: TypeAlias = list[
    "aws_sdk_sagemaker.types.cfn_stack_update_parameter.CfnStackUpdateParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnStackUpdateParameters) -> list:
    import aws_sdk_sagemaker.types.cfn_stack_update_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.cfn_stack_update_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CfnStackUpdateParameters:
    import aws_sdk_sagemaker.types.cfn_stack_update_parameter

    out: CfnStackUpdateParameters = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.cfn_stack_update_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
