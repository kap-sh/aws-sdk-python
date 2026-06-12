"""Generated from Smithy shape ``com.amazonaws.sagemaker#CategoricalParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.categorical_parameter

CategoricalParameters: TypeAlias = list[
    "aws_sdk_sagemaker.types.categorical_parameter.CategoricalParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CategoricalParameters) -> list:
    import aws_sdk_sagemaker.types.categorical_parameter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.categorical_parameter.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CategoricalParameters:
    import aws_sdk_sagemaker.types.categorical_parameter

    out: CategoricalParameters = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.categorical_parameter.deserialize_aws_json_1_1(item)
        )
    return out
