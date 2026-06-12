"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#LoginsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_provider_name

LoginsList: TypeAlias = list[
    "aws_sdk_cognito_identity.types.identity_provider_name.IdentityProviderName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoginsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> LoginsList:
    return list(data)
