"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#MessageActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

MessageActionType: TypeAlias = Literal[
    "RESEND",
    "SUPPRESS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESEND",
        "SUPPRESS",
    )
)


def serialize_aws_json_1_1(value: MessageActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MessageActionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MessageActionType value: {data!r}")
    return cast(MessageActionType, data)
