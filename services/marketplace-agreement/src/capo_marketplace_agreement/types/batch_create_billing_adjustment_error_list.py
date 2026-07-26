"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#BatchCreateBillingAdjustmentErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_error

BatchCreateBillingAdjustmentErrorList: TypeAlias = list[
    "capo_marketplace_agreement.types.batch_create_billing_adjustment_error.BatchCreateBillingAdjustmentError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateBillingAdjustmentErrorList) -> list:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_error

    out: list = []
    for item in value:
        out.append(
            capo_marketplace_agreement.types.batch_create_billing_adjustment_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BatchCreateBillingAdjustmentErrorList:
    import capo_marketplace_agreement.types.batch_create_billing_adjustment_error

    out: BatchCreateBillingAdjustmentErrorList = []
    for item in data:
        out.append(
            capo_marketplace_agreement.types.batch_create_billing_adjustment_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
