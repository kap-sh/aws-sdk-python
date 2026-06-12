"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IdentityProviderTypeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

IdentityProviderTypeType: TypeAlias = Literal[
    "SAML",
    "Facebook",
    "Google",
    "LoginWithAmazon",
    "SignInWithApple",
    "OIDC",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SAML",
        "Facebook",
        "Google",
        "LoginWithAmazon",
        "SignInWithApple",
        "OIDC",
    )
)


def serialize_aws_json_1_1(value: IdentityProviderTypeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityProviderTypeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown IdentityProviderTypeType value: {data!r}")
    return cast(IdentityProviderTypeType, data)
