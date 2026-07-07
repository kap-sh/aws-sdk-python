"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstancePool``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.instance_pool_priority
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.production_variant_instance_type


class InstancePool(TypedDict, closed=True):
    instance_type: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_instance_type.ProductionVariantInstanceType"
    ]
    """<p>The ML compute instance type for the instance pool.</p>"""
    model_name_override: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of a SageMaker model to use for this instance pool instead of the model specified for the production variant. Use this to deploy a different model optimized for the instance type in this pool.</p>"""
    priority: NotRequired[
        "aws_sdk_sagemaker.types.instance_pool_priority.InstancePoolPriority"
    ]
    """<p>The priority for the instance pool. SageMaker attempts to provision instances in order of priority, starting with the lowest value. If instances for a higher-priority pool are unavailable, SageMaker attempts to provision from the next pool.</p> <p>Valid values: 1 to 5, where 1 is the highest priority.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePool) -> dict:
    out: dict = {}
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "model_name_override" in value:
        out["ModelNameOverride"] = value["model_name_override"]
    if "priority" in value:
        out["Priority"] = value["priority"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstancePool:
    out: InstancePool = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.production_variant_instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.production_variant_instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "ModelNameOverride" in data:
        out["model_name_override"] = data["ModelNameOverride"]
    if "Priority" in data:
        out["priority"] = data["Priority"]
    return out
