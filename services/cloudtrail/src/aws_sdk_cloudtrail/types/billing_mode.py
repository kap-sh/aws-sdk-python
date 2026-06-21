"""Generated from Smithy shape ``com.amazonaws.cloudtrail#BillingMode``."""

from typing import Literal, TypeAlias, cast

BillingMode: TypeAlias = Literal[
    "EXTENDABLE_RETENTION_PRICING",
    "FIXED_RETENTION_PRICING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BillingMode:
    return cast(BillingMode, data)
