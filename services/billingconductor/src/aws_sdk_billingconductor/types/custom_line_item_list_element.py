"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemListElement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.computation_rule_enum
    import aws_sdk_billingconductor.types.currency_code
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_description
    import aws_sdk_billingconductor.types.custom_line_item_name
    import aws_sdk_billingconductor.types.custom_line_item_product_code
    import aws_sdk_billingconductor.types.instant
    import aws_sdk_billingconductor.types.list_custom_line_item_charge_details
    import aws_sdk_billingconductor.types.number_of_associations
    import aws_sdk_billingconductor.types.presentation_object


class CustomLineItemListElement(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p>The Amazon Resource Names (ARNs) for custom line items.</p>"""
    name: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p>The custom line item's name.</p>"""
    charge_details: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    """<p>A <code>ListCustomLineItemChargeDetails</code> that describes the charge details of a custom line item.</p>"""
    currency_code: NotRequired[
        "aws_sdk_billingconductor.types.currency_code.CurrencyCode"
    ]
    """<p>The custom line item's charge value currency. Only one of the valid values can be used.</p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p>The custom line item's description. This is shown on the Bills page in association with the charge value.</p>"""
    product_code: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_product_code.CustomLineItemProductCode"
    ]
    """<p>The product code that's associated with the custom line item.</p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.</p>"""
    creation_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The time created.</p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The most recent time when the custom line item was modified.</p>"""
    association_size: (
        "aws_sdk_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p>The number of resources that are associated to the custom line item.</p>"""
    account_id: NotRequired["aws_sdk_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account in which this custom line item will be applied to.</p>"""
    computation_rule: NotRequired[
        "aws_sdk_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
    ]
    """<p> The computation rule that determines how the custom line item charges are computed and reflected in the bill. </p>"""
    presentation_details: NotRequired[
        "aws_sdk_billingconductor.types.presentation_object.PresentationObject"
    ]
    """<p> Configuration details specifying how the custom line item charges are presented, including which service the charges are shown under. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemListElement) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "charge_details" in value:
        import aws_sdk_billingconductor.types.list_custom_line_item_charge_details

        out["ChargeDetails"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_charge_details.serialize_json(
                value["charge_details"]
            )
        )
    if "currency_code" in value:
        import aws_sdk_billingconductor.types.currency_code

        out["CurrencyCode"] = (
            aws_sdk_billingconductor.types.currency_code.serialize_json(
                value["currency_code"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "product_code" in value:
        out["ProductCode"] = value["product_code"]
    if "billing_group_arn" in value:
        out["BillingGroupArn"] = value["billing_group_arn"]
    out["CreationTime"] = value.get("creation_time", 0)
    out["LastModifiedTime"] = value.get("last_modified_time", 0)
    out["AssociationSize"] = value.get("association_size", 0)
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    if "computation_rule" in value:
        import aws_sdk_billingconductor.types.computation_rule_enum

        out["ComputationRule"] = (
            aws_sdk_billingconductor.types.computation_rule_enum.serialize_json(
                value["computation_rule"]
            )
        )
    if "presentation_details" in value:
        import aws_sdk_billingconductor.types.presentation_object

        out["PresentationDetails"] = (
            aws_sdk_billingconductor.types.presentation_object.serialize_json(
                value["presentation_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> CustomLineItemListElement:
    out: CustomLineItemListElement = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ChargeDetails" in data:
        import aws_sdk_billingconductor.types.list_custom_line_item_charge_details

        out["charge_details"] = (
            aws_sdk_billingconductor.types.list_custom_line_item_charge_details.deserialize_json(
                data["ChargeDetails"]
            )
        )
    if "CurrencyCode" in data:
        import aws_sdk_billingconductor.types.currency_code

        out["currency_code"] = (
            aws_sdk_billingconductor.types.currency_code.deserialize_json(
                data["CurrencyCode"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "ProductCode" in data:
        out["product_code"] = data["ProductCode"]
    if "BillingGroupArn" in data:
        out["billing_group_arn"] = data["BillingGroupArn"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    else:
        out["creation_time"] = 0
    if "LastModifiedTime" in data:
        out["last_modified_time"] = data["LastModifiedTime"]
    else:
        out["last_modified_time"] = 0
    if "AssociationSize" in data:
        out["association_size"] = data["AssociationSize"]
    else:
        out["association_size"] = 0
    if "AccountId" in data:
        out["account_id"] = data["AccountId"]
    if "ComputationRule" in data:
        import aws_sdk_billingconductor.types.computation_rule_enum

        out["computation_rule"] = (
            aws_sdk_billingconductor.types.computation_rule_enum.deserialize_json(
                data["ComputationRule"]
            )
        )
    if "PresentationDetails" in data:
        import aws_sdk_billingconductor.types.presentation_object

        out["presentation_details"] = (
            aws_sdk_billingconductor.types.presentation_object.deserialize_json(
                data["PresentationDetails"]
            )
        )
    return out
