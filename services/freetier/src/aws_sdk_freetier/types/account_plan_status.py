"""Generated from Smithy shape ``com.amazonaws.freetier#AccountPlanStatus``."""

from typing import Literal, TypeAlias, cast

AccountPlanStatus: TypeAlias = Literal[
    "NOT_STARTED",
    "ACTIVE",
    "EXPIRED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountPlanStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountPlanStatus:
    return cast(AccountPlanStatus, data)
