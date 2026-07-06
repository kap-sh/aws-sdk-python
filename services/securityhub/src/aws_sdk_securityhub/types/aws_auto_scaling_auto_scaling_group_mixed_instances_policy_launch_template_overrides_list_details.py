"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails(
    TypedDict, closed=True
):
    instance_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The instance type. For example, <code>m3.xlarge</code>.</p>"""
    weighted_capacity: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The number of capacity units provided by the specified instance type in terms of virtual CPUs, memory, storage, throughput, or other relative performance characteristic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails,
) -> dict:
    out: dict = {}
    if "instance_type" in value:
        out["InstanceType"] = value["instance_type"]
    if "weighted_capacity" in value:
        out["WeightedCapacity"] = value["weighted_capacity"]
    return out


def deserialize_json(
    data: dict,
) -> (
    AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails
):
    out: AwsAutoScalingAutoScalingGroupMixedInstancesPolicyLaunchTemplateOverridesListDetails = {}  # type: ignore[typeddict-item]
    if "InstanceType" in data:
        out["instance_type"] = data["InstanceType"]
    if "WeightedCapacity" in data:
        out["weighted_capacity"] = data["WeightedCapacity"]
    return out
