"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemChargeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_flat_charge_details
    import aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details
    import aws_sdk_billingconductor.types.custom_line_item_type
    import aws_sdk_billingconductor.types.line_item_filters_list


class CustomLineItemChargeDetails(TypedDict, closed=True):
    flat: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_flat_charge_details.CustomLineItemFlatChargeDetails"
    ]
    """<p>A <code>CustomLineItemFlatChargeDetails</code> that describes the charge details of a flat custom line item.</p>"""
    percentage: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details.CustomLineItemPercentageChargeDetails"
    ]
    """<p>A <code>CustomLineItemPercentageChargeDetails</code> that describes the charge details of a percentage custom line item.</p>"""
    type: "aws_sdk_billingconductor.types.custom_line_item_type.CustomLineItemType"
    """<p>The type of the custom line item that indicates whether the charge is a fee or credit.</p>"""
    line_item_filters: NotRequired[
        "aws_sdk_billingconductor.types.line_item_filters_list.LineItemFiltersList"
    ]
    """<p>A representation of the line item filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemChargeDetails) -> dict:
    out: dict = {}
    if "flat" in value:
        import aws_sdk_billingconductor.types.custom_line_item_flat_charge_details

        out["Flat"] = (
            aws_sdk_billingconductor.types.custom_line_item_flat_charge_details.serialize_json(
                value["flat"]
            )
        )
    if "percentage" in value:
        import aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details

        out["Percentage"] = (
            aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details.serialize_json(
                value["percentage"]
            )
        )
    import aws_sdk_billingconductor.types.custom_line_item_type

    out["Type"] = aws_sdk_billingconductor.types.custom_line_item_type.serialize_json(
        value["type"]
    )
    if "line_item_filters" in value:
        import aws_sdk_billingconductor.types.line_item_filters_list

        out["LineItemFilters"] = (
            aws_sdk_billingconductor.types.line_item_filters_list.serialize_json(
                value["line_item_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLineItemChargeDetails:
    out: CustomLineItemChargeDetails = {}  # type: ignore[typeddict-item]
    if "Flat" in data:
        import aws_sdk_billingconductor.types.custom_line_item_flat_charge_details

        out["flat"] = (
            aws_sdk_billingconductor.types.custom_line_item_flat_charge_details.deserialize_json(
                data["Flat"]
            )
        )
    if "Percentage" in data:
        import aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details

        out["percentage"] = (
            aws_sdk_billingconductor.types.custom_line_item_percentage_charge_details.deserialize_json(
                data["Percentage"]
            )
        )
    if "Type" in data:
        import aws_sdk_billingconductor.types.custom_line_item_type

        out["type"] = (
            aws_sdk_billingconductor.types.custom_line_item_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CustomLineItemChargeDetails.type required")
    if "LineItemFilters" in data:
        import aws_sdk_billingconductor.types.line_item_filters_list

        out["line_item_filters"] = (
            aws_sdk_billingconductor.types.line_item_filters_list.deserialize_json(
                data["LineItemFilters"]
            )
        )
    return out
