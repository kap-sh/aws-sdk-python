"""Generated from Smithy shape ``com.amazonaws.sagemaker#ProductionVariantManagedInstanceScaling``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.managed_instance_scaling_max_instance_count
    import aws_sdk_sagemaker.types.managed_instance_scaling_min_instance_count
    import aws_sdk_sagemaker.types.managed_instance_scaling_status
    import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy


class ProductionVariantManagedInstanceScaling(TypedDict):
    status: NotRequired[
        "aws_sdk_sagemaker.types.managed_instance_scaling_status.ManagedInstanceScalingStatus"
    ]
    """<p>Indicates whether managed instance scaling is enabled.</p>"""
    min_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.managed_instance_scaling_min_instance_count.ManagedInstanceScalingMinInstanceCount"
    ]
    """<p>The minimum number of instances that the endpoint must retain when it scales down to accommodate a decrease in traffic.</p>"""
    max_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.managed_instance_scaling_max_instance_count.ManagedInstanceScalingMaxInstanceCount"
    ]
    """<p>The maximum number of instances that the endpoint can provision when it scales up to accommodate an increase in traffic.</p>"""
    scale_in_policy: NotRequired[
        "aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy.ProductionVariantManagedInstanceScalingScaleInPolicy"
    ]
    """<p>Configures the scale-in behavior for managed instance scaling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProductionVariantManagedInstanceScaling) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_sagemaker.types.managed_instance_scaling_status

        out["Status"] = (
            aws_sdk_sagemaker.types.managed_instance_scaling_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "min_instance_count" in value:
        out["MinInstanceCount"] = value["min_instance_count"]
    if "max_instance_count" in value:
        out["MaxInstanceCount"] = value["max_instance_count"]
    if "scale_in_policy" in value:
        import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy

        out["ScaleInPolicy"] = (
            aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy.serialize_aws_json_1_1(
                value["scale_in_policy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProductionVariantManagedInstanceScaling:
    out: ProductionVariantManagedInstanceScaling = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_sagemaker.types.managed_instance_scaling_status

        out["status"] = (
            aws_sdk_sagemaker.types.managed_instance_scaling_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "MinInstanceCount" in data:
        out["min_instance_count"] = data["MinInstanceCount"]
    if "MaxInstanceCount" in data:
        out["max_instance_count"] = data["MaxInstanceCount"]
    if "ScaleInPolicy" in data:
        import aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy

        out["scale_in_policy"] = (
            aws_sdk_sagemaker.types.production_variant_managed_instance_scaling_scale_in_policy.deserialize_aws_json_1_1(
                data["ScaleInPolicy"]
            )
        )
    return out
