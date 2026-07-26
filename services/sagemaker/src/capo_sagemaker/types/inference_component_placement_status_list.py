"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentPlacementStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.inference_component_placement_status

InferenceComponentPlacementStatusList: TypeAlias = list[
    "capo_sagemaker.types.inference_component_placement_status.InferenceComponentPlacementStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentPlacementStatusList) -> list:
    import capo_sagemaker.types.inference_component_placement_status

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.inference_component_placement_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InferenceComponentPlacementStatusList:
    import capo_sagemaker.types.inference_component_placement_status

    out: InferenceComponentPlacementStatusList = []
    for item in data:
        out.append(
            capo_sagemaker.types.inference_component_placement_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
