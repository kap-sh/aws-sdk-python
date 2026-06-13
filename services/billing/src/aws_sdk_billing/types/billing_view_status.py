"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_billing.errors import DeserializationError

BillingViewStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "CREATING",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEALTHY",
        "UNHEALTHY",
        "CREATING",
        "UPDATING",
    )
)


def serialize_aws_json_1_0(value: BillingViewStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown BillingViewStatus value: {data!r}")
    return cast(BillingViewStatus, data)
