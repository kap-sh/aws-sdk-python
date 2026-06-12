"""Generated from Smithy shape ``com.amazonaws.sagemaker#OutputParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.output_parameter

OutputParameterList: TypeAlias = list[
    "aws_sdk_sagemaker.types.output_parameter.OutputParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OutputParameterList) -> list:
    import aws_sdk_sagemaker.types.output_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.output_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OutputParameterList:
    import aws_sdk_sagemaker.types.output_parameter

    out: OutputParameterList = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.output_parameter.deserialize_aws_json_1_1(item)
        )
    return out
