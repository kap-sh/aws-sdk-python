"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CompromisedCredentialsEventActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

CompromisedCredentialsEventActionType: TypeAlias = Literal[
    "BLOCK",
    "NO_ACTION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BLOCK",
        "NO_ACTION",
    )
)


def serialize_aws_json_1_1(value: CompromisedCredentialsEventActionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CompromisedCredentialsEventActionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CompromisedCredentialsEventActionType value: {data!r}"
        )
    return cast(CompromisedCredentialsEventActionType, data)
