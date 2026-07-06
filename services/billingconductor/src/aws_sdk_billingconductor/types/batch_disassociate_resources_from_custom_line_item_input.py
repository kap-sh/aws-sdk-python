"""Generated from Smithy shape ``com.amazonaws.billingconductor#BatchDisassociateResourcesFromCustomLineItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list
    import aws_sdk_billingconductor.types.custom_line_item_billing_period_range


class BatchDisassociateResourcesFromCustomLineItemInput(TypedDict, closed=True):
    target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> A percentage custom line item ARN to disassociate the resources from. </p>"""
    resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list.CustomLineItemBatchDisassociationsList"
    """<p> A list containing the ARNs of resources to be disassociated. </p>"""
    billing_period_range: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDisassociateResourcesFromCustomLineItemInput) -> dict:
    out: dict = {}
    out["TargetArn"] = value["target_arn"]
    import aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list

    out["ResourceArns"] = (
        aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list.serialize_json(
            value["resource_arns"]
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


def deserialize_json(data: dict) -> BatchDisassociateResourcesFromCustomLineItemInput:
    out: BatchDisassociateResourcesFromCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError(
            "BatchDisassociateResourcesFromCustomLineItemInput.target_arn required"
        )
    if "ResourceArns" in data:
        import aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list

        out["resource_arns"] = (
            aws_sdk_billingconductor.types.custom_line_item_batch_disassociations_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError(
            "BatchDisassociateResourcesFromCustomLineItemInput.resource_arns required"
        )
    if "BillingPeriodRange" in data:
        import aws_sdk_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            aws_sdk_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
