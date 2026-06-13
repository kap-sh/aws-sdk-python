"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billing.errors import DeserializationError

BillingViewType: TypeAlias = Literal[
    "PRIMARY",
    "BILLING_GROUP",
    "CUSTOM",
    "BILLING_TRANSFER",
    "BILLING_TRANSFER_SHOWBACK",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRIMARY",
        "BILLING_GROUP",
        "CUSTOM",
        "BILLING_TRANSFER",
        "BILLING_TRANSFER_SHOWBACK",
    )
)


def serialize_aws_json_1_0(value: BillingViewType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingViewType value: {data!r}")
    return cast(BillingViewType, data)
