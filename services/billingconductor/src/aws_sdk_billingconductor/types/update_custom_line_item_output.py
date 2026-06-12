"""Generated from Smithy shape ``com.amazonaws.billingconductor#UpdateCustomLineItemOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.billing_group_full_arn
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_description
    import aws_sdk_billingconductor.types.custom_line_item_name
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.list_custom_line_item_charge_details
    import aws_sdk_billingconductor.types.number_of_associations


class UpdateCustomLineItemOutput(TypedDict):
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> The ARN of the successfully updated custom line item. </p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_full_arn.BillingGroupFullArn"
    ]
    """<p> The ARN of the billing group that the custom line item is applied to. </p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p> The name of the successfully updated custom line item. </p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p> The description of the successfully updated custom line item. </p>"""
    charge_details: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    """<p> A <code>ListCustomLineItemChargeDetails</code> containing the charge details of the successfully updated custom line item. </p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p> The most recent time when the custom line item was modified. </p>"""
    association_size: (
        "aws_sdk_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p> The number of resources that are associated to the custom line item. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCustomLineItemOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "charge_details" in value:
        import aws_sdk_billingconductor.types.list_custom_line_item_charge_details

        out["ChargeDetails"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    out["AssociationSize"] = value.get("association_size", 0)
    return out


def deserialize_json(data: dict) -> UpdateCustomLineItemOutput:
    out: UpdateCustomLineItemOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "BillingGroupArn" in data:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "ChargeDetails" in data:
        import aws_sdk_billingconductor.types.list_custom_line_item_charge_details

        out["charge_details"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "AssociationSize" in data:
        out["association_size"] = data["AssociationSize"]
    else:
        out["association_size"] = 0
    return out
