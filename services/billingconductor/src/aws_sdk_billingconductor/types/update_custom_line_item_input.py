"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_billing_period_range
    import aws_sdk_billingconductor.types.custom_line_item_description
    import aws_sdk_billingconductor.types.custom_line_item_name
    import aws_sdk_billingconductor.types.update_custom_line_item_charge_details


class UpdateCustomLineItemInput(TypedDict):
    arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> The ARN of the custom line item to be updated. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p> The new name for the custom line item. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p> The new line item description of the custom line item. </p>"""
    charge_details: NotRequired[
        "aws_sdk_billingconductor.types.update_custom_line_item_charge_details.UpdateCustomLineItemChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemChargeDetails</code> containing the new charge details for the custom line item. </p>"""
    billing_period_range: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemInput) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "charge_details" in value:
        import aws_sdk_billingconductor.types.update_custom_line_item_charge_details

        out["ChargeDetails"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    if "billing_period_range" in value:
        import aws_sdk_billingconductor.types.custom_line_item_billing_period_range

        out["BillingPeriodRange"] = (
            aws_sdk_billingconductor.types.custom_line_item_billing_period_range.serialize_json(
                value["billing_period_range"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemInput:
    out: UpdateCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("UpdateCustomLineItemInput.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ChargeDetails" in data:
        import aws_sdk_billingconductor.types.update_custom_line_item_charge_details

        out["charge_details"] = (
            aws_sdk_billingconductor.types.update_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if "BillingPeriodRange" in data:
        import aws_sdk_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            aws_sdk_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
