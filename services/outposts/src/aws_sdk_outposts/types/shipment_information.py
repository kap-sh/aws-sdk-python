"""Generated from Smithy shape ``com.amazonaws.outposts#ShipmentInformation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.shipment_carrier
    import aws_sdk_outposts.types.tracking_id


class ShipmentInformation(TypedDict):
    shipment_tracking_number: NotRequired[
        "aws_sdk_outposts.types.tracking_id.TrackingId"
    ]
    """<p> The tracking number of the shipment. </p>"""
    shipment_carrier: NotRequired[
        "aws_sdk_outposts.types.shipment_carrier.ShipmentCarrier"
    ]
    """<p> The carrier of the shipment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ShipmentInformation) -> dict:
    out: dict = {}
    if "shipment_tracking_number" in value:
        out["ShipmentTrackingNumber"] = value["shipment_tracking_number"]
    if "shipment_carrier" in value:
        import aws_sdk_outposts.types.shipment_carrier

        out["ShipmentCarrier"] = aws_sdk_outposts.types.shipment_carrier.serialize_json(
            value["shipment_carrier"]
        )
    return out


def deserialize_json(data: dict) -> ShipmentInformation:
    out: ShipmentInformation = {}  # type: ignore[typeddict-item]
    if "ShipmentTrackingNumber" in data:
        out["shipment_tracking_number"] = data["ShipmentTrackingNumber"]
    if "ShipmentCarrier" in data:
        import aws_sdk_outposts.types.shipment_carrier

        out["shipment_carrier"] = (
            aws_sdk_outposts.types.shipment_carrier.deserialize_json(
                data["ShipmentCarrier"]
            )
        )
    return out
