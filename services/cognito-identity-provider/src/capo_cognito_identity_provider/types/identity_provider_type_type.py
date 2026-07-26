"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IdentityProviderTypeType``."""

from typing import Literal, TypeAlias, cast

IdentityProviderTypeType: TypeAlias = Literal[
    "SAML",
    "Facebook",
    "Google",
    "LoginWithAmazon",
    "SignInWithApple",
    "OIDC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderTypeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityProviderTypeType:
    return cast(IdentityProviderTypeType, data)
