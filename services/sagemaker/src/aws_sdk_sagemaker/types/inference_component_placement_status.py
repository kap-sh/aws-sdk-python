"""Generated from Smithy shape ``com.amazonaws.sagemaker#InferenceComponentPlacementStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.inference_component_copy_count
    import aws_sdk_sagemaker.types.production_variant_instance_type


class InferenceComponentPlacementStatus(TypedDict, closed=True):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type where the inference component copies are placed.</p>"""
    current_copy_count: NotRequired[
        "aws_sdk_sagemaker.types.inference_component_copy_count.InferenceComponentCopyCount"
    ]
    """<p>The number of inference component copies currently placed on instances of this type.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InferenceComponentPlacementStatus) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "current_copy_count" in value:
        out["CurrentCopyCount"] = value["current_copy_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InferenceComponentPlacementStatus:
    out: InferenceComponentPlacementStatus = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "CurrentCopyCount" in data:
        out["current_copy_count"] = data["CurrentCopyCount"]
    return out
