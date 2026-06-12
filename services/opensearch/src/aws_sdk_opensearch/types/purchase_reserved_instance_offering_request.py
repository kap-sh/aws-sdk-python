"""Generated from Smithy shape ``com.amazonaws.opensearch#PurchaseReservedInstanceOfferingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.guid
    import aws_sdk_opensearch.types.instance_count
    import aws_sdk_opensearch.types.reservation_token


class PurchaseReservedInstanceOfferingRequest(TypedDict):
    reserved_instance_offering_id: "aws_sdk_opensearch.types.guid.GUID"
    """<p>The ID of the Reserved Instance offering to purchase.</p>"""
    reservation_name: "aws_sdk_opensearch.types.reservation_token.ReservationToken"
    """<p>A customer-specified identifier to track this reservation.</p>"""
    instance_count: NotRequired["aws_sdk_opensearch.types.instance_count.InstanceCount"]
    """<p>The number of OpenSearch instances to reserve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseReservedInstanceOfferingRequest) -> dict:
    out: dict = {}
    out["ReservedInstanceOfferingId"] = value["reserved_instance_offering_id"]
    out["ReservationName"] = value["reservation_name"]
    if "instance_count" in value:
        out["InstanceCount"] = value["instance_count"]
    return out


def deserialize_json(data: dict) -> PurchaseReservedInstanceOfferingRequest:
    out: PurchaseReservedInstanceOfferingRequest = {}  # type: ignore[typeddict-item]
    if "ReservedInstanceOfferingId" in data:
        out["reserved_instance_offering_id"] = data["ReservedInstanceOfferingId"]
    else:
        raise DeserializationError(
            "PurchaseReservedInstanceOfferingRequest.reserved_instance_offering_id required"
        )
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    else:
        raise DeserializationError(
            "PurchaseReservedInstanceOfferingRequest.reservation_name required"
        )
    if "InstanceCount" in data:
        out["instance_count"] = data["InstanceCount"]
    return out
