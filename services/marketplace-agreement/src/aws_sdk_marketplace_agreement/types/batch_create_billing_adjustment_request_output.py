"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list


class BatchCreateBillingAdjustmentRequestOutput(TypedDict):
    items: "aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list.BatchCreateBillingAdjustmentItemList"
    """<p>A list of successfully created billing adjustment items, each containing the <code>billingAdjustmentRequestId</code> and <code>clientToken</code>.</p>"""
    errors: "aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list.BatchCreateBillingAdjustmentErrorList"
    """<p>A list of errors for entries that failed validation, each containing the <code>clientToken</code>, error <code>code</code>, and <code>message</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestOutput) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list

    out["items"] = (
        aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list.serialize_aws_json_1_0(
            value["items"]
        )
    )
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list

    out["errors"] = (
        aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list.serialize_aws_json_1_0(
            value["errors"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentRequestOutput:
    out: BatchCreateBillingAdjustmentRequestOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list

        out["items"] = (
            aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_item_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestOutput.items required"
        )
    if "errors" in data:
        import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list

        out["errors"] = (
            aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_error_list.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestOutput.errors required"
        )
    return out
