"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ReceiptType``."""

from typing import Literal, TypeAlias, cast

ReceiptType: TypeAlias = Literal[
    "DELIVERED",
    "ERROR",
    "READ",
    "SENT",
    "STOP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceiptType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ReceiptType:
    return cast(ReceiptType, data)
