"""Generated from Smithy shape ``com.amazonaws.devicefarm#OfferingTransactionType``."""

from typing import Literal, TypeAlias, cast

OfferingTransactionType: TypeAlias = Literal[
    "PURCHASE",
    "RENEW",
    "SYSTEM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OfferingTransactionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OfferingTransactionType:
    return cast(OfferingTransactionType, data)
