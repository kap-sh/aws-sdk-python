"""Generated from Smithy shape ``com.amazonaws.sagemaker#Ec2CapacityReservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.ec2_capacity_reservation_id
    import aws_sdk_sagemaker.types.task_count


class Ec2CapacityReservation(TypedDict):
    ec2_capacity_reservation_id: NotRequired[
        "aws_sdk_sagemaker.types.ec2_capacity_reservation_id.Ec2CapacityReservationId"
    ]
    """<p>The unique identifier for an EC2 capacity reservation that's part of the ML capacity reservation.</p>"""
    total_instance_count: NotRequired["aws_sdk_sagemaker.types.task_count.TaskCount"]
    """<p>The number of instances that you allocated to the EC2 capacity reservation.</p>"""
    available_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.task_count.TaskCount"
    ]
    """<p>The number of instances that are currently available in the EC2 capacity reservation.</p>"""
    used_by_current_endpoint: NotRequired[
        "aws_sdk_sagemaker.types.task_count.TaskCount"
    ]
    """<p>The number of instances from the EC2 capacity reservation that are being used by the endpoint.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2CapacityReservation) -> dict:
    out: dict = {}
    if "ec2_capacity_reservation_id" in value:
        out["Ec2CapacityReservationId"] = value["ec2_capacity_reservation_id"]
    if "total_instance_count" in value:
        out["TotalInstanceCount"] = value["total_instance_count"]
    if "available_instance_count" in value:
        out["AvailableInstanceCount"] = value["available_instance_count"]
    if "used_by_current_endpoint" in value:
        out["UsedByCurrentEndpoint"] = value["used_by_current_endpoint"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Ec2CapacityReservation:
    out: Ec2CapacityReservation = {}  # type: ignore[typeddict-item]
    if "Ec2CapacityReservationId" in data:
        out["ec2_capacity_reservation_id"] = data["Ec2CapacityReservationId"]
    if "TotalInstanceCount" in data:
        out["total_instance_count"] = data["TotalInstanceCount"]
    if "AvailableInstanceCount" in data:
        out["available_instance_count"] = data["AvailableInstanceCount"]
    if "UsedByCurrentEndpoint" in data:
        out["used_by_current_endpoint"] = data["UsedByCurrentEndpoint"]
    return out
