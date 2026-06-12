"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#EmailSendingAccountType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

EmailSendingAccountType: TypeAlias = Literal[
    "COGNITO_DEFAULT",
    "DEVELOPER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "COGNITO_DEFAULT",
        "DEVELOPER",
    )
)


def serialize_aws_json_1_1(value: EmailSendingAccountType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EmailSendingAccountType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EmailSendingAccountType value: {data!r}")
    return cast(EmailSendingAccountType, data)
