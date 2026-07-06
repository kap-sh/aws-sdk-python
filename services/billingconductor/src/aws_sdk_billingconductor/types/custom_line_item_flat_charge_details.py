"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemFlatChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_charge_value


class CustomLineItemFlatChargeDetails(TypedDict, closed=True):
    charge_value: "aws_sdk_billingconductor.types.custom_line_item_charge_value.CustomLineItemChargeValue"
    """<p>The custom line item's fixed charge value in USD.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemFlatChargeDetails) -> dict:
    out: dict = {}
    out["ChargeValue"] = value["charge_value"]
    return out


def deserialize_json(data: dict) -> CustomLineItemFlatChargeDetails:
    out: CustomLineItemFlatChargeDetails = {}  # type: ignore[typeddict-item]
    if "ChargeValue" in data:
        out["charge_value"] = data["ChargeValue"]
    else:
        raise DeserializationError(
            "CustomLineItemFlatChargeDetails.charge_value required"
        )
    return out
