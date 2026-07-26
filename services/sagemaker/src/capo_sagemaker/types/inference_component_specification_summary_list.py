"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentSpecificationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_specification_summary

InferenceComponentSpecificationSummaryList: TypeAlias = list[
    "capo_sagemaker.types.inference_component_specification_summary.InferenceComponentSpecificationSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentSpecificationSummaryList) -> list:
    import capo_sagemaker.types.inference_component_specification_summary

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_component_specification_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceComponentSpecificationSummaryList:
    import capo_sagemaker.types.inference_component_specification_summary

    out: InferenceComponentSpecificationSummaryList = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_component_specification_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
