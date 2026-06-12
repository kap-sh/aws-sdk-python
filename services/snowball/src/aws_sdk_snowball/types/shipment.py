"""Generated from Smithy shape ``com.amazonaws.snowball#Shipment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_snowball.types.string


class Shipment(TypedDict):
    status: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>Status information for a shipment.</p>"""
    tracking_number: NotRequired["aws_sdk_snowball.types.string.String"]
    """<p>The tracking number for this job. Using this tracking number with your region's carrier's website, you can track a Snow device as the carrier transports it.</p> <p>For India, the carrier is Amazon Logistics. For all other regions, UPS is the carrier.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Shipment) -> dict:
    out: dict = {}
    if "status" in value:
        out["Status"] = value["status"]
    if "tracking_number" in value:
        out["TrackingNumber"] = value["tracking_number"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Shipment:
    out: Shipment = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        out["status"] = data["Status"]
    if "TrackingNumber" in data:
        out["tracking_number"] = data["TrackingNumber"]
    return out
