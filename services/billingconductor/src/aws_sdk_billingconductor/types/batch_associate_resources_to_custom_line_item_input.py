"""Generated from Smithy shape ``com.amazonaws.billingconductor#BatchAssociateResourcesToCustomLineItemInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_billingconductor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.custom_line_item_arn
    import aws_sdk_billingconductor.types.custom_line_item_batch_associations_list
    import aws_sdk_billingconductor.types.custom_line_item_billing_period_range


class BatchAssociateResourcesToCustomLineItemInput(TypedDict, closed=True):
    target_arn: "aws_sdk_billingconductor.types.custom_line_item_arn.CustomLineItemArn"
    """<p> A percentage custom line item ARN to associate the resources to. </p>"""
    resource_arns: "aws_sdk_billingconductor.types.custom_line_item_batch_associations_list.CustomLineItemBatchAssociationsList"
    """<p> A list containing the ARNs of the resources to be associated. </p>"""
    billing_period_range: NotRequired[
        "aws_sdk_billingconductor.types.custom_line_item_billing_period_range.CustomLineItemBillingPeriodRange"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchAssociateResourcesToCustomLineItemInput) -> dict:
    out: dict = {}
    out["TargetArn"] = value["target_arn"]
    import aws_sdk_billingconductor.types.custom_line_item_batch_associations_list

    out["ResourceArns"] = (
        aws_sdk_billingconductor.types.custom_line_item_batch_associations_list.serialize_json(
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


def deserialize_json(data: dict) -> BatchAssociateResourcesToCustomLineItemInput:
    out: BatchAssociateResourcesToCustomLineItemInput = {}  # type: ignore[typeddict-item]
    if "TargetArn" in data:
        out["target_arn"] = data["TargetArn"]
    else:
        raise DeserializationError(
            "BatchAssociateResourcesToCustomLineItemInput.target_arn required"
        )
    if "ResourceArns" in data:
        import aws_sdk_billingconductor.types.custom_line_item_batch_associations_list

        out["resource_arns"] = (
            aws_sdk_billingconductor.types.custom_line_item_batch_associations_list.deserialize_json(
                data["ResourceArns"]
            )
        )
    else:
        raise DeserializationError(
            "BatchAssociateResourcesToCustomLineItemInput.resource_arns required"
        )
    if "BillingPeriodRange" in data:
        import aws_sdk_billingconductor.types.custom_line_item_billing_period_range

        out["billing_period_range"] = (
            aws_sdk_billingconductor.types.custom_line_item_billing_period_range.deserialize_json(
                data["BillingPeriodRange"]
            )
        )
    return out
