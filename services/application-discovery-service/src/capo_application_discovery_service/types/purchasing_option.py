"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#PurchasingOption``."""

from typing import Literal, TypeAlias, cast

PurchasingOption: TypeAlias = Literal[
    "ALL_UPFRONT",
    "PARTIAL_UPFRONT",
    "NO_UPFRONT",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PurchasingOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PurchasingOption:
    return cast(PurchasingOption, data)
