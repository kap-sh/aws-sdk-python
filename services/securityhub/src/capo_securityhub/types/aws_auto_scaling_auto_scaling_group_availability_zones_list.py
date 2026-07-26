"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAutoScalingAutoScalingGroupAvailabilityZonesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details

AwsAutoScalingAutoScalingGroupAvailabilityZonesList: TypeAlias = list[
    "capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details.AwsAutoScalingAutoScalingGroupAvailabilityZonesListDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsAutoScalingAutoScalingGroupAvailabilityZonesList) -> list:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsAutoScalingAutoScalingGroupAvailabilityZonesList:
    import capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details

    out: AwsAutoScalingAutoScalingGroupAvailabilityZonesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_auto_scaling_auto_scaling_group_availability_zones_list_details.deserialize_json(
                item
            )
        )
    return out
