"""Generated from Smithy shape ``com.amazonaws.opensearch#PurchaseReservedInstanceOfferingResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearch.types.guid
    import capo_opensearch.types.reservation_token


class PurchaseReservedInstanceOfferingResponse(TypedDict, closed=True):
    reserved_instance_id: NotRequired["capo_opensearch.types.guid.GUID"]
    """<p>The ID of the Reserved Instance offering that was purchased.</p>"""
    reservation_name: NotRequired[
        "capo_opensearch.types.reservation_token.ReservationToken"
    ]
    """<p>The customer-specified identifier used to track this reservation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PurchaseReservedInstanceOfferingResponse) -> dict:
    out: dict = {}
    if "reserved_instance_id" in value:
        out["ReservedInstanceId"] = value["reserved_instance_id"]
    if "reservation_name" in value:
        out["ReservationName"] = value["reservation_name"]
    return out


def deserialize_json(data: dict) -> PurchaseReservedInstanceOfferingResponse:
    out: PurchaseReservedInstanceOfferingResponse = {}  # type: ignore[typeddict-item]
    if "ReservedInstanceId" in data:
        out["reserved_instance_id"] = data["ReservedInstanceId"]
    if "ReservationName" in data:
        out["reservation_name"] = data["ReservationName"]
    return out
