"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyper_parameter_specification

HyperParameterSpecifications: TypeAlias = list[
    "aws_sdk_sagemaker.types.hyper_parameter_specification.HyperParameterSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterSpecifications) -> list:
    import aws_sdk_sagemaker.types.hyper_parameter_specification

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.hyper_parameter_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HyperParameterSpecifications:
    import aws_sdk_sagemaker.types.hyper_parameter_specification

    out: HyperParameterSpecifications = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.hyper_parameter_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
