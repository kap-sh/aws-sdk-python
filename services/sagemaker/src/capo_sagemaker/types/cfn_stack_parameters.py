"""Generated from Smithy shape ``com.amazonaws.sagemaker#CfnStackParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.cfn_stack_parameter

CfnStackParameters: TypeAlias = list[
    "capo_sagemaker.types.cfn_stack_parameter.CfnStackParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CfnStackParameters) -> list:
    import capo_sagemaker.types.cfn_stack_parameter

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.cfn_stack_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CfnStackParameters:
    import capo_sagemaker.types.cfn_stack_parameter

    out: CfnStackParameters = []
    for item in data:
        out.append(
            capo_sagemaker.types.cfn_stack_parameter.deserialize_aws_json_1_1(item)
        )
    return out
