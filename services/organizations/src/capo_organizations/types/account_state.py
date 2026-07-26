"""Generated from Smithy shape ``com.amazonaws.organizations#AccountState``."""

from typing import Literal, TypeAlias, cast

AccountState: TypeAlias = Literal[
    "PENDING_ACTIVATION",
    "ACTIVE",
    "SUSPENDED",
    "PENDING_CLOSURE",
    "CLOSED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountState:
    return cast(AccountState, data)
