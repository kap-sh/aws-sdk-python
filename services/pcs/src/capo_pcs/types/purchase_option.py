"""Generated from Smithy shape ``com.amazonaws.pcs#PurchaseOption``."""

from typing import Literal, TypeAlias, cast

PurchaseOption: TypeAlias = Literal[
    "ONDEMAND",
    "SPOT",
    "CAPACITY_BLOCK",
    "INTERRUPTIBLE_CAPACITY_RESERVATION",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PurchaseOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PurchaseOption:
    return cast(PurchaseOption, data)
