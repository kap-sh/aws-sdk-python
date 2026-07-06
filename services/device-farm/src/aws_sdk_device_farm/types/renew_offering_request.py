"""Generated from Smithy shape ``com.amazonaws.devicefarm#RenewOfferingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.offering_identifier


class RenewOfferingRequest(TypedDict, closed=True):
    offering_id: "aws_sdk_device_farm.types.offering_identifier.OfferingIdentifier"
    """<p>The ID of a request to renew an offering.</p>"""
    quantity: "aws_sdk_device_farm.types.integer.Integer"
    """<p>The quantity requested in an offering renewal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RenewOfferingRequest) -> dict:
    out: dict = {}
    out["offeringId"] = value["offering_id"]
    out["quantity"] = value["quantity"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RenewOfferingRequest:
    out: RenewOfferingRequest = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    else:
        raise DeserializationError("RenewOfferingRequest.offering_id required")
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    else:
        raise DeserializationError("RenewOfferingRequest.quantity required")
    return out
