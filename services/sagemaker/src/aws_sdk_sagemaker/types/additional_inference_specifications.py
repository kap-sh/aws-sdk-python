"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalInferenceSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_inference_specification_definition

AdditionalInferenceSpecifications: TypeAlias = list[
    "aws_sdk_sagemaker.types.additional_inference_specification_definition.AdditionalInferenceSpecificationDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalInferenceSpecifications) -> list:
    import aws_sdk_sagemaker.types.additional_inference_specification_definition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker.types.additional_inference_specification_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalInferenceSpecifications:
    import aws_sdk_sagemaker.types.additional_inference_specification_definition

    out: AdditionalInferenceSpecifications = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.additional_inference_specification_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
