"""Generated from Smithy shape ``com.amazonaws.dynamodb#BillingMode``."""

from typing import Literal, TypeAlias, cast

BillingMode: TypeAlias = Literal[
    "PROVISIONED",
    "PAY_PER_REQUEST",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillingMode:
    return cast(BillingMode, data)
