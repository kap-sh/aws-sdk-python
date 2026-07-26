"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#PaymentFrequency``."""

from typing import Literal, TypeAlias, cast

PaymentFrequency: TypeAlias = Literal["Monthly",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PaymentFrequency) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PaymentFrequency:
    return cast(PaymentFrequency, data)
