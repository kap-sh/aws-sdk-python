"""Generated from Smithy shape ``com.amazonaws.sagemaker#AdditionalInferenceSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.additional_inference_specification_definition

AdditionalInferenceSpecifications: TypeAlias = list[
    "capo_sagemaker.types.additional_inference_specification_definition.AdditionalInferenceSpecificationDefinition"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdditionalInferenceSpecifications) -> list:
    import capo_sagemaker.types.additional_inference_specification_definition

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.additional_inference_specification_definition.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AdditionalInferenceSpecifications:
    import capo_sagemaker.types.additional_inference_specification_definition

    out: AdditionalInferenceSpecifications = []
    for item in data:
        out.append(
            capo_sagemaker.types.additional_inference_specification_definition.deserialize_aws_json_1_1(
                item
            )
        )
    return out
