"""Generated from Smithy shape ``com.amazonaws.sagemaker#InstanceGroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.capacity_reservation
    import aws_sdk_sagemaker.types.security_group_ids


class InstanceGroupMetadata(TypedDict, closed=True):
    failure_message: NotRequired["str"]
    """<p>An error message describing why the instance group level operation (such as creating, scaling, or deleting) failed.</p>"""
    availability_zone_id: NotRequired["str"]
    """<p>The ID of the Availability Zone where the instance group is located.</p>"""
    capacity_reservation: NotRequired[
        "aws_sdk_sagemaker.types.capacity_reservation.CapacityReservation"
    ]
    """<p>Information about the Capacity Reservation used by the instance group.</p>"""
    subnet_id: NotRequired["str"]
    """<p>The ID of the subnet where the instance group is located.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>A list of security group IDs associated with the instance group.</p>"""
    ami_override: NotRequired["str"]
    """<p>If you use a custom Amazon Machine Image (AMI) for the instance group, this field shows the ID of the custom AMI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceGroupMetadata) -> dict:
    out: dict = {}
    if "failure_message" in value:
        out["FailureMessage"] = value["failure_message"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    if "capacity_reservation" in value:
        import aws_sdk_sagemaker.types.capacity_reservation

        out["CapacityReservation"] = (
            aws_sdk_sagemaker.types.capacity_reservation.serialize_aws_json_1_1(
                value["capacity_reservation"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "ami_override" in value:
        out["AmiOverride"] = value["ami_override"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceGroupMetadata:
    out: InstanceGroupMetadata = {}  # type: ignore[typeddict-item]
    if "FailureMessage" in data:
        out["failure_message"] = data["FailureMessage"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "CapacityReservation" in data:
        import aws_sdk_sagemaker.types.capacity_reservation

        out["capacity_reservation"] = (
            aws_sdk_sagemaker.types.capacity_reservation.deserialize_aws_json_1_1(
                data["CapacityReservation"]
            )
        )
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "AmiOverride" in data:
        out["ami_override"] = data["AmiOverride"]
    return out
