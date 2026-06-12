"""Generated from Smithy shape ``com.amazonaws.sagemaker#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.parameter

ParameterList: TypeAlias = list["aws_sdk_sagemaker.types.parameter.Parameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterList) -> list:
    import aws_sdk_sagemaker.types.parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterList:
    import aws_sdk_sagemaker.types.parameter

    out: ParameterList = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.parameter.deserialize_aws_json_1_1(item))
    return out
