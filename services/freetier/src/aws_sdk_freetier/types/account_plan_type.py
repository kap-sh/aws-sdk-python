"""Generated from Smithy shape ``com.amazonaws.freetier#AccountPlanType``."""

from typing import Literal, TypeAlias, cast

AccountPlanType: TypeAlias = Literal[
    "FREE",
    "PAID",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountPlanType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountPlanType:
    return cast(AccountPlanType, data)
