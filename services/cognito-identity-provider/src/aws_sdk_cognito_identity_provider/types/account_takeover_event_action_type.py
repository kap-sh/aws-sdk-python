"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AccountTakeoverEventActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

AccountTakeoverEventActionType: TypeAlias = Literal[
    "BLOCK",
    "MFA_IF_CONFIGURED",
    "MFA_REQUIRED",
    "NO_ACTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "MFA_IF_CONFIGURED",
        "MFA_REQUIRED",
        "NO_ACTION",
    )
)


def serialize_aws_json_1_1(value: AccountTakeoverEventActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountTakeoverEventActionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AccountTakeoverEventActionType value: {data!r}"
        )
    return cast(AccountTakeoverEventActionType, data)
