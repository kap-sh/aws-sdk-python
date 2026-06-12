"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_provider_id
    import aws_sdk_cognito_identity.types.identity_provider_name

IdentityProviders: TypeAlias = dict[
    "aws_sdk_cognito_identity.types.identity_provider_name.IdentityProviderName",
    "aws_sdk_cognito_identity.types.identity_provider_id.IdentityProviderId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: IdentityProviders) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityProviders:
    out: IdentityProviders = {}
    for key, value in data.items():
        out[key] = value
    return out
