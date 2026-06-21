"""Generated from Smithy shape ``com.amazonaws.licensemanager#CheckoutType``."""

from typing import Literal, TypeAlias, cast

CheckoutType: TypeAlias = Literal[
    "PROVISIONAL",
    "PERPETUAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CheckoutType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CheckoutType:
    return cast(CheckoutType, data)
