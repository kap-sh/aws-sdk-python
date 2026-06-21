"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewType``."""

from typing import Literal, TypeAlias, cast

BillingViewType: TypeAlias = Literal[
    "PRIMARY",
    "BILLING_GROUP",
    "CUSTOM",
    "BILLING_TRANSFER",
    "BILLING_TRANSFER_SHOWBACK",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewType:
    return cast(BillingViewType, data)
