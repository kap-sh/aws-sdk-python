"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentRequestEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

BatchCreateBillingAdjustmentRequestEntryList: TypeAlias = list[
    "aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.BatchCreateBillingAdjustmentRequestEntry"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentRequestEntryList) -> list:
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(
    data: list,
) -> BatchCreateBillingAdjustmentRequestEntryList:
    import aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry

    out: BatchCreateBillingAdjustmentRequestEntryList = []
    for item in data:
        out.append(
            aws_sdk_marketplace_agreement.types.batch_create_billing_adjustment_request_entry.deserialize_aws_json_1_0(
                item
            )
        )
    return out
