"""Generated from Smithy shape ``com.amazonaws.workmail#IdentityProviderAuthenticationMode``."""

from typing import Literal, TypeAlias, cast

IdentityProviderAuthenticationMode: TypeAlias = Literal[
    "IDENTITY_PROVIDER_ONLY",
    "IDENTITY_PROVIDER_AND_DIRECTORY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdentityProviderAuthenticationMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IdentityProviderAuthenticationMode:
    return cast(IdentityProviderAuthenticationMode, data)
