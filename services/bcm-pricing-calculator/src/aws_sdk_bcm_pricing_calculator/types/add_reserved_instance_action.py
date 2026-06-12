"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#AddReservedInstanceAction``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.reserved_instance_instance_count
    import aws_sdk_bcm_pricing_calculator.types.uuid

class AddReservedInstanceAction(TypedDict):
    reserved_instances_offering_id: NotRequired["aws_sdk_bcm_pricing_calculator.types.uuid.Uuid"]
    """<p> The ID of the Reserved Instance offering to add. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeReservedInstancesOfferings.html\"> DescribeReservedInstancesOfferings</a>. </p>"""
    instance_count: NotRequired["aws_sdk_bcm_pricing_calculator.types.reserved_instance_instance_count.ReservedInstanceInstanceCount"]
    """<p> The number of instances to add for this Reserved Instance offering. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AddReservedInstanceAction) -> dict:
    out: dict = {}
    if "reserved_instances_offering_id" in value:
        out["reservedInstancesOfferingId"] = value["reserved_instances_offering_id"]
    if "instance_count" in value:
        out["instanceCount"] = value["instance_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AddReservedInstanceAction:
    out: AddReservedInstanceAction = {}  # type: ignore[typeddict-item]
    if "reservedInstancesOfferingId" in data:
        out["reserved_instances_offering_id"] = data["reservedInstancesOfferingId"]
    if "instanceCount" in data:
        out["instance_count"] = data["instanceCount"]
    return out