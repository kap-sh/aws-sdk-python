"""Generated from Smithy shape ``com.amazonaws.billingconductor#ListCustomLineItemFlatChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_charge_value


class ListCustomLineItemFlatChargeDetails(TypedDict, closed=True):
    charge_value: "capo_billingconductor.types.custom_line_item_charge_value.CustomLineItemChargeValue"
    """<p> The custom line item's fixed charge value in USD. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCustomLineItemFlatChargeDetails) -> dict:
    out: dict = {}
    out["ChargeValue"] = value["charge_value"]
    return out


def deserialize_json(data: dict) -> ListCustomLineItemFlatChargeDetails:
    out: ListCustomLineItemFlatChargeDetails = {}  # type: ignore[typeddict-item]
    if "ChargeValue" in data:
        out["charge_value"] = data["ChargeValue"]
    else:
        raise DeserializationError(
            "ListCustomLineItemFlatChargeDetails.charge_value required"
        )
    return out
