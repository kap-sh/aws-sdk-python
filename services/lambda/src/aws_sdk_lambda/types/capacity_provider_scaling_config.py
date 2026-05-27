"""Generated from Smithy shape ``com.amazonaws.lambda#CapacityProviderScalingConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.capacity_provider_max_v_cpu_count
    import aws_sdk_lambda.types.capacity_provider_scaling_mode
    import aws_sdk_lambda.types.capacity_provider_scaling_policies_list


class CapacityProviderScalingConfig(TypedDict):
    max_v_cpu_count: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_max_v_cpu_count.CapacityProviderMaxVCpuCount"
    ]
    """<p>The maximum number of vCPUs that the capacity provider can provision across all compute instances.</p>"""
    scaling_mode: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_scaling_mode.CapacityProviderScalingMode"
    ]
    """<p>The scaling mode that determines how the capacity provider responds to changes in demand.</p>"""
    scaling_policies: NotRequired[
        "aws_sdk_lambda.types.capacity_provider_scaling_policies_list.CapacityProviderScalingPoliciesList"
    ]
    """<p>A list of scaling policies that define how the capacity provider scales compute instances based on metrics and thresholds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityProviderScalingConfig) -> dict:
    out: dict = {}
    if "max_v_cpu_count" in value:
        out["MaxVCpuCount"] = value["max_v_cpu_count"]
    if "scaling_mode" in value:
        import aws_sdk_lambda.types.capacity_provider_scaling_mode

        out["ScalingMode"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_mode.serialize_json(
                value["scaling_mode"]
            )
        )
    if "scaling_policies" in value:
        import aws_sdk_lambda.types.capacity_provider_scaling_policies_list

        out["ScalingPolicies"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_policies_list.serialize_json(
                value["scaling_policies"]
            )
        )
    return out


def deserialize_json(data: dict) -> CapacityProviderScalingConfig:
    out: CapacityProviderScalingConfig = {}  # type: ignore[typeddict-item]
    if "MaxVCpuCount" in data:
        out["max_v_cpu_count"] = data["MaxVCpuCount"]
    if "ScalingMode" in data:
        import aws_sdk_lambda.types.capacity_provider_scaling_mode

        out["scaling_mode"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_mode.deserialize_json(
                data["ScalingMode"]
            )
        )
    if "ScalingPolicies" in data:
        import aws_sdk_lambda.types.capacity_provider_scaling_policies_list

        out["scaling_policies"] = (
            aws_sdk_lambda.types.capacity_provider_scaling_policies_list.deserialize_json(
                data["ScalingPolicies"]
            )
        )
    return out
