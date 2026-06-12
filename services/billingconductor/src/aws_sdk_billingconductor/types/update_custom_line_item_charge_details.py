"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemChargeDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.line_item_filters_list
    import aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details
    import aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details


class UpdateCustomLineItemChargeDetails(TypedDict):
    flat: NotRequired[
        "aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details.UpdateCustomLineItemFlatChargeDetails"
    ]
    """<p> An <code>UpdateCustomLineItemFlatChargeDetails</code> that describes the new charge details of a flat custom line item. </p>"""
    percentage: NotRequired[
        "aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details.UpdateCustomLineItemPercentageChargeDetails"
    ]
    """<p> An <code>UpdateCustomLineItemPercentageChargeDetails</code> that describes the new charge details of a percentage custom line item. </p>"""
    line_item_filters: NotRequired[
        "aws_sdk_billingconductor.types.line_item_filters_list.LineItemFiltersList"
    ]
    """<p>A representation of the line item filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemChargeDetails) -> dict:
    out: dict = {}
    if "flat" in value:
        import aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details

        out["Flat"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details.serialize_json(
                value["flat"]
            )
        )
    if "percentage" in value:
        import aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details

        out["Percentage"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details.serialize_json(
                value["percentage"]
            )
        )
    if "line_item_filters" in value:
        import aws_sdk_billingconductor.types.line_item_filters_list

        out["LineItemFilters"] = (
            aws_sdk_billingconductor.types.line_item_filters_list.serialize_json(
                value["line_item_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemChargeDetails:
    out: UpdateCustomLineItemChargeDetails = {}  # type: ignore[typeddict-item]
    if "Flat" in data:
        import aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details

        out["flat"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_flat_charge_details.deserialize_json(
                data["Flat"]
            )
        )
    if "Percentage" in data:
        import aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details

        out["percentage"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_percentage_charge_details.deserialize_json(
                data["Percentage"]
            )
        )
    if "LineItemFilters" in data:
        import aws_sdk_billingconductor.types.line_item_filters_list

        out["line_item_filters"] = (
            aws_sdk_billingconductor.types.line_item_filters_list.deserialize_json(
                data["LineItemFilters"]
            )
        )
    return out
