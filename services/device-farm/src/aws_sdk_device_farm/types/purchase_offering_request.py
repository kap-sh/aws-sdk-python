"""Generated from Smithy shape ``com.amazonaws.devicefarm#PurchaseOfferingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.integer
    import aws_sdk_device_farm.types.offering_identifier
    import aws_sdk_device_farm.types.offering_promotion_identifier


class PurchaseOfferingRequest(TypedDict):
    offering_id: "aws_sdk_device_farm.types.offering_identifier.OfferingIdentifier"
    """<p>The ID of the offering.</p>"""
    quantity: "aws_sdk_device_farm.types.integer.Integer"
    """<p>The number of device slots to purchase in an offering request.</p>"""
    offering_promotion_id: NotRequired[
        "aws_sdk_device_farm.types.offering_promotion_identifier.OfferingPromotionIdentifier"
    ]
    """<p>The ID of the offering promotion to be applied to the purchase.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchaseOfferingRequest) -> dict:
    out: dict = {}
    out["offeringId"] = value["offering_id"]
    out["quantity"] = value["quantity"]
    if "offering_promotion_id" in value:
        out["offeringPromotionId"] = value["offering_promotion_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PurchaseOfferingRequest:
    out: PurchaseOfferingRequest = {}  # type: ignore[typeddict-item]
    if "offeringId" in data:
        out["offering_id"] = data["offeringId"]
    else:
        raise DeserializationError("PurchaseOfferingRequest.offering_id required")
    if "quantity" in data:
        out["quantity"] = data["quantity"]
    else:
        raise DeserializationError("PurchaseOfferingRequest.quantity required")
    if "offeringPromotionId" in data:
        out["offering_promotion_id"] = data["offeringPromotionId"]
    return out
