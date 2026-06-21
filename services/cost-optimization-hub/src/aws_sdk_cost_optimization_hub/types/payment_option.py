"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#PaymentOption``."""

from typing import Literal, TypeAlias, cast

PaymentOption: TypeAlias = Literal[
    "AllUpfront",
    "PartialUpfront",
    "NoUpfront",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentOption) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentOption:
    return cast(PaymentOption, data)
