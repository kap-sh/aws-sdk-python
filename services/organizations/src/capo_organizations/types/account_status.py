"""Generated from Smithy shape ``com.amazonaws.organizations#AccountStatus``."""

from typing import Literal, TypeAlias, cast

AccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "SUSPENDED",
    "PENDING_CLOSURE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountStatus:
    return cast(AccountStatus, data)
