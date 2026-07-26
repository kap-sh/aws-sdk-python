"""Generated from Smithy shape ``com.amazonaws.invoicing#BillType``."""

from typing import Literal, TypeAlias, cast

BillType: TypeAlias = Literal[
    "ANNIVERSARY",
    "PURCHASE",
    "REFUND",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> BillType:
    return cast(BillType, data)
