"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverEventActionType``."""

from typing import Literal, TypeAlias, cast

AccountTakeoverEventActionType: TypeAlias = Literal[
    "BLOCK",
    "MFA_IF_CONFIGURED",
    "MFA_REQUIRED",
    "NO_ACTION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountTakeoverEventActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountTakeoverEventActionType:
    return cast(AccountTakeoverEventActionType, data)
