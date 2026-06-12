"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingPromotion``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.message
    import aws_sdk_device_farm.types.offering_promotion_identifier


class OfferingPromotion(TypedDict):
    id: NotRequired[
        "aws_sdk_device_farm.types.offering_promotion_identifier.OfferingPromotionIdentifier"
    ]
    """<p>The ID of the offering promotion.</p>"""
    description: NotRequired["aws_sdk_device_farm.types.message.Message"]
    """<p>A string that describes the offering promotion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingPromotion) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> OfferingPromotion:
    out: OfferingPromotion = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "description" in data:
        out["description"] = data["description"]
    return out
