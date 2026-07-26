"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_specification

InferenceComponentSpecificationList: TypeAlias = list[
    "capo_sagemaker.types.inference_component_specification.InferenceComponentSpecification"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSpecificationList) -> list:
    import capo_sagemaker.types.inference_component_specification

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_component_specification.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceComponentSpecificationList:
    import capo_sagemaker.types.inference_component_specification

    out: InferenceComponentSpecificationList = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_component_specification.deserialize_aws_json_1_1(
                item
            )
        )
    return out
