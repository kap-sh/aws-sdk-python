"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemPercentageChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_associations_list
    import capo_billingconductor.types.custom_line_item_percentage_charge_value


class CustomLineItemPercentageChargeDetails(TypedDict, closed=True):
    percentage_value: "capo_billingconductor.types.custom_line_item_percentage_charge_value.CustomLineItemPercentageChargeValue"
    """<p>The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value. </p>"""
    associated_values: NotRequired[
        "capo_billingconductor.types.custom_line_item_associations_list.CustomLineItemAssociationsList"
    ]
    """<p>A list of resource ARNs to associate to the percentage custom line item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemPercentageChargeDetails) -> dict:
    out: dict = {}
    out["PercentageValue"] = value["percentage_value"]
    if "associated_values" in value:
        import capo_billingconductor.types.custom_line_item_associations_list

        out["AssociatedValues"] = (
            capo_billingconductor.types.custom_line_item_associations_list.serialize_json(
                value["associated_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLineItemPercentageChargeDetails:
    out: CustomLineItemPercentageChargeDetails = {}  # type: ignore[typeddict-item]
    if "PercentageValue" in data:
        out["percentage_value"] = data["PercentageValue"]
    else:
        raise DeserializationError(
            "CustomLineItemPercentageChargeDetails.percentage_value required"
        )
    if "AssociatedValues" in data:
        import capo_billingconductor.types.custom_line_item_associations_list

        out["associated_values"] = (
            capo_billingconductor.types.custom_line_item_associations_list.deserialize_json(
                data["AssociatedValues"]
            )
        )
    return out
