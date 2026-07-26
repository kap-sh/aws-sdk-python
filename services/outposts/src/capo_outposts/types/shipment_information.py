"""Generated from Smithy shape ``com.amazonaws.outposts#ShipmentInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.shipment_carrier
    import capo_outposts.types.tracking_id


class ShipmentInformation(TypedDict, closed=True):
    shipment_tracking_number: NotRequired["capo_outposts.types.tracking_id.TrackingId"]
    """<p> The tracking number of the shipment. </p>"""
    shipment_carrier: NotRequired[
        "capo_outposts.types.shipment_carrier.ShipmentCarrier"
    ]
    """<p> The carrier of the shipment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShipmentInformation) -> dict:
    out: dict = {}
    if "shipment_tracking_number" in value:
        out["ShipmentTrackingNumber"] = value["shipment_tracking_number"]
    if "shipment_carrier" in value:
        import capo_outposts.types.shipment_carrier

        out["ShipmentCarrier"] = capo_outposts.types.shipment_carrier.serialize_json(
            value["shipment_carrier"]
        )
    return out


def deserialize_json(data: dict) -> ShipmentInformation:
    out: ShipmentInformation = {}  # type: ignore[typeddict-item]
    if "ShipmentTrackingNumber" in data:
        out["shipment_tracking_number"] = data["ShipmentTrackingNumber"]
    if "ShipmentCarrier" in data:
        import capo_outposts.types.shipment_carrier

        out["shipment_carrier"] = capo_outposts.types.shipment_carrier.deserialize_json(
            data["ShipmentCarrier"]
        )
    return out
