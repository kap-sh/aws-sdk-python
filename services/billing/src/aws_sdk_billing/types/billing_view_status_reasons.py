"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_status_reason

BillingViewStatusReasons: TypeAlias = list[
    "aws_sdk_billing.types.billing_view_status_reason.BillingViewStatusReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewStatusReasons) -> list:
    import aws_sdk_billing.types.billing_view_status_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_billing.types.billing_view_status_reason.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewStatusReasons:
    import aws_sdk_billing.types.billing_view_status_reason

    out: BillingViewStatusReasons = []
    for item in data:
        out.append(
            aws_sdk_billing.types.billing_view_status_reason.deserialize_aws_json_1_0(
                item
            )
        )
    return out
