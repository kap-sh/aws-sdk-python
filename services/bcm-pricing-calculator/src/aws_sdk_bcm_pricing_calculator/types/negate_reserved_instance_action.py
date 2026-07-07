"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#NegateReservedInstanceAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.uuid


class NegateReservedInstanceAction(TypedDict, closed=True):
    reserved_instances_id: NotRequired["aws_sdk_bcm_pricing_calculator.types.uuid.Uuid"]
    """<p> The ID of the Reserved Instance to remove. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NegateReservedInstanceAction) -> dict:
    out: dict = {}
    if "reserved_instances_id" in value:
        out["reservedInstancesId"] = value["reserved_instances_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> NegateReservedInstanceAction:
    out: NegateReservedInstanceAction = {}  # type: ignore[typeddict-item]
    if "reservedInstancesId" in data:
        out["reserved_instances_id"] = data["reservedInstancesId"]
    return out
