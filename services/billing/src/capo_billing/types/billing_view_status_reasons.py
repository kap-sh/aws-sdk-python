"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatusReasons``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_billing.types.billing_view_status_reason

BillingViewStatusReasons: TypeAlias = list[
    "capo_billing.types.billing_view_status_reason.BillingViewStatusReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewStatusReasons) -> list:
    import capo_billing.types.billing_view_status_reason

    out: list = []
    for item in value:
        out.append(
            capo_billing.types.billing_view_status_reason.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BillingViewStatusReasons:
    import capo_billing.types.billing_view_status_reason

    out: BillingViewStatusReasons = []
    for item in data:
        out.append(
            capo_billing.types.billing_view_status_reason.deserialize_aws_json_1_0(item)
        )
    return out
