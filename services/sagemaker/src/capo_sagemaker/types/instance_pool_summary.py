"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePoolSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.production_variant_instance_type
    import capo_sagemaker.types.task_count


class InstancePoolSummary(TypedDict, closed=True):
    instance_type: NotRequired[
        "capo_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type for the instance pool.</p>"""
    current_instance_count: NotRequired["capo_sagemaker.types.task_count.TaskCount"]
    """<p>The current number of instances of this type in the instance pool.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePoolSummary) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import capo_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            capo_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "current_instance_count" in value:
        out["CurrentInstanceCount"] = value["current_instance_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePoolSummary:
    out: InstancePoolSummary = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import capo_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            capo_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "CurrentInstanceCount" in data:
        out["current_instance_count"] = data["CurrentInstanceCount"]
    return out
