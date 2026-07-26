"""Generated from Smithy shape ``com.amazonaws.devicefarm#BillingMethod``."""

from typing import Literal, TypeAlias, cast

BillingMethod: TypeAlias = Literal[
    "METERED",
    "UNMETERED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BillingMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> BillingMethod:
    return cast(BillingMethod, data)
