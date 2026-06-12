"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#CognitoIdentityProviderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.cognito_identity_provider

CognitoIdentityProviderList: TypeAlias = list[
    "aws_sdk_cognito_identity.types.cognito_identity_provider.CognitoIdentityProvider"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CognitoIdentityProviderList) -> list:
    import aws_sdk_cognito_identity.types.cognito_identity_provider

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity.types.cognito_identity_provider.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CognitoIdentityProviderList:
    import aws_sdk_cognito_identity.types.cognito_identity_provider

    out: CognitoIdentityProviderList = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity.types.cognito_identity_provider.deserialize_aws_json_1_1(
                item
            )
        )
    return out
