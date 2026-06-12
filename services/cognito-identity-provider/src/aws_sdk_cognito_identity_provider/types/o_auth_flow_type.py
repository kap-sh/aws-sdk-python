"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#OAuthFlowType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

OAuthFlowType: TypeAlias = Literal[
    "code",
    "implicit",
    "client_credentials",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "code",
        "implicit",
        "client_credentials",
    )
)


def serialize_aws_json_1_1(value: OAuthFlowType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OAuthFlowType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OAuthFlowType value: {data!r}")
    return cast(OAuthFlowType, data)
