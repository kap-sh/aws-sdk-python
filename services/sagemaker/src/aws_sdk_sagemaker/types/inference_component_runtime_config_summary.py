"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentRuntimeConfigSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_copy_count
    import aws_sdk_sagemaker.types.inference_component_placement_status_list


class InferenceComponentRuntimeConfigSummary(TypedDict):
    desired_copy_count: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_copy_count.InferenceComponentCopyCount"
    ]
    """<p>The number of runtime copies of the model container that you requested to deploy with the inference component.</p>"""
    current_copy_count: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_copy_count.InferenceComponentCopyCount"
    ]
    """<p>The number of runtime copies of the model container that are currently deployed.</p>"""
    placement_status: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_placement_status_list.InferenceComponentPlacementStatusList"
    ]
    """<p>The placement status of the inference component across instance types. Shows how the inference component copies are distributed across instance types.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentRuntimeConfigSummary) -> dict:
    out: dict = {}
    if "desired_copy_count" in value:
        out["DesiredCopyCount"] = value["desired_copy_count"]
    if "current_copy_count" in value:
        out["CurrentCopyCount"] = value["current_copy_count"]
    if "placement_status" in value:
        import aws_sdk_sagemaker.types.inference_component_placement_status_list

        out["PlacementStatus"] = (
            aws_sdk_sagemaker.types.inference_component_placement_status_list.serialize_aws_json_1_1(
                value["placement_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentRuntimeConfigSummary:
    out: InferenceComponentRuntimeConfigSummary = {}  # type: ignore[typeddict-item]
    if "DesiredCopyCount" in data:
        out["desired_copy_count"] = data["DesiredCopyCount"]
    if "CurrentCopyCount" in data:
        out["current_copy_count"] = data["CurrentCopyCount"]
    if "PlacementStatus" in data:
        import aws_sdk_sagemaker.types.inference_component_placement_status_list

        out["placement_status"] = (
            aws_sdk_sagemaker.types.inference_component_placement_status_list.deserialize_aws_json_1_1(
                data["PlacementStatus"]
            )
        )
    return out
