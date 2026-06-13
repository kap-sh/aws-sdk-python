"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list


class BatchCreateBillingAdjustmentRequestInput(TypedDict):
    billing_adjustment_request_entries: "aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.BatchCreateBillingAdjustmentRequestEntryList"
    """<p>A list of billing adjustment request entries. Each entry specifies the invoice and adjustment details.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestInput) -> dict:
    out: dict = {}
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list

    out["billingAdjustmentRequestEntries"] = (
        aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.serialize_aws_json_1_0(
            value["billing_adjustment_request_entries"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateBillingAdjustmentRequestInput:
    out: BatchCreateBillingAdjustmentRequestInput = {}  # type: ignore[typeddict-item]
    if "billingAdjustmentRequestEntries" in data:
        import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list

        out["billing_adjustment_request_entries"] = (
            aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry_list.deserialize_aws_json_1_0(
                data["billingAdjustmentRequestEntries"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateBillingAdjustmentRequestInput.billing_adjustment_request_entries required"
        )
    return out
