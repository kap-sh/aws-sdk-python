"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CapacityReservationTarget``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.arn
    import aws_sdk_workspaces_instances.types.string128

class CapacityReservationTarget(TypedDict):
    capacity_reservation_id: NotRequired["aws_sdk_workspaces_instances.types.string128.String128"]
    """<p>Unique identifier for the capacity reservation.</p>"""
    capacity_reservation_resource_group_arn: NotRequired["aws_sdk_workspaces_instances.types.arn.ARN"]
    """<p>ARN of the capacity reservation resource group.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityReservationTarget) -> dict:
    out: dict = {}
    if "capacity_reservation_id" in value:
        out["CapacityReservationId"] = value["capacity_reservation_id"]
    if "capacity_reservation_resource_group_arn" in value:
        out["CapacityReservationResourceGroupArn"] = value["capacity_reservation_resource_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityReservationTarget:
    out: CapacityReservationTarget = {}  # type: ignore[typeddict-item]
    if "CapacityReservationId" in data:
        out["capacity_reservation_id"] = data["CapacityReservationId"]
    if "CapacityReservationResourceGroupArn" in data:
        out["capacity_reservation_resource_group_arn"] = data["CapacityReservationResourceGroupArn"]
    return out