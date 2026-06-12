"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemVersionListElement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.account_id
    import aws_sdk_billingconductor.types.billing_group_arn
    import aws_sdk_billingconductor.types.billing_period
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


class CustomLineItemVersionListElement(TypedDict):
    name: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_name.CustomLineItemName"
    ]
    """<p>The name of the custom line item.</p>"""
    charge_details: NotRequired[
        "aws_sdk_billingconductor.types.list_custom_line_item_charge_details.ListCustomLineItemChargeDetails"
    ]
    currency_code: NotRequired[
        "aws_sdk_billingconductor.types.currency_code.CurrencyCode"
    ]
    """<p>The charge value currency of the custom line item.</p>"""
    description: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_description.CustomLineItemDescription"
    ]
    """<p>The description of the custom line item.</p>"""
    product_code: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_product_code.CustomLineItemProductCode"
    ]
    """<p>The product code that’s associated with the custom line item.</p>"""
    billing_group_arn: NotRequired[
        "aws_sdk_billingconductor.types.billing_group_arn.BillingGroupArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the billing group that the custom line item applies to.</p>"""
    creation_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The time when the custom line item version was created.</p>"""
    last_modified_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p>The most recent time that the custom line item version was modified.</p>"""
    association_size: (
        "aws_sdk_billingconductor.types.number_of_associations.NumberOfAssociations"
    )
    """<p>The number of resources that are associated with the custom line item.</p>"""
    start_billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The start billing period of the custom line item version.</p>"""
    end_billing_period: NotRequired[
        "aws_sdk_billingconductor.types.billing_period.BillingPeriod"
    ]
    """<p>The end billing period of the custom line item version.</p>"""
    arn: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    ]
    """<p> A list of custom line item Amazon Resource Names (ARNs) to retrieve information. </p>"""
    start_time: "aws_sdk_billingconductor.types.instant.Instant"
    """<p> The inclusive start time. </p>"""
    account_id: NotRequired["aws_sdk_billingconductor.types.account_id.AccountId"]
    """<p>The Amazon Web Services account in which this custom line item will be applied to.</p>"""
    computation_rule: NotRequired[
        "aws_sdk_billingconductor.types.computation_rule_enum.ComputationRuleEnum"
    ]
    """<p> The computation rule for a specific version of a custom line item, determining how charges are computed and reflected in the bill. </p>"""
    presentation_details: NotRequired[
        "aws_sdk_billingconductor.types.presentation_object.PresentationObject"
    ]
    """<p> Presentation configuration for a specific version of a custom line item, specifying how charges are displayed in the bill. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemVersionListElement) -> dict:
    out: dict = {}
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
    if "start_billing_period" in value:
        out["StartBillingPeriod"] = value["start_billing_period"]
    if "end_billing_period" in value:
        out["EndBillingPeriod"] = value["end_billing_period"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    out["StartTime"] = value.get("start_time", 0)
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


def deserialize_json(data: dict) -> CustomLineItemVersionListElement:
    out: CustomLineItemVersionListElement = {}  # type: ignore[typeddict-item]
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
    if "StartBillingPeriod" in data:
        out["start_billing_period"] = data["StartBillingPeriod"]
    if "EndBillingPeriod" in data:
        out["end_billing_period"] = data["EndBillingPeriod"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = 0
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
