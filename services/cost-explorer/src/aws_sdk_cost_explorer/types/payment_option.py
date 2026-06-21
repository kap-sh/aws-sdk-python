"""Generated from Smithy shape ``com.amazonaws.costexplorer#PaymentOption``."""

from typing import Literal, TypeAlias, cast

PaymentOption: TypeAlias = Literal[
    "NO_UPFRONT",
    "PARTIAL_UPFRONT",
    "ALL_UPFRONT",
    "LIGHT_UTILIZATION",
    "MEDIUM_UTILIZATION",
    "HEAVY_UTILIZATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PaymentOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PaymentOption:
    return cast(PaymentOption, data)
