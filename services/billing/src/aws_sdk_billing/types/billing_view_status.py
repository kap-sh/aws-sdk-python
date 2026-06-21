"""Generated from Smithy shape ``com.amazonaws.billing#BillingViewStatus``."""

from typing import Literal, TypeAlias, cast

BillingViewStatus: TypeAlias = Literal[
    "HEALTHY",
    "UNHEALTHY",
    "CREATING",
    "UPDATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingViewStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingViewStatus:
    return cast(BillingViewStatus, data)
