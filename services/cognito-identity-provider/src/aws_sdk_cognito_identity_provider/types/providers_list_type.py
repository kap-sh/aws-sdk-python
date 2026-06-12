"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ProvidersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.provider_description

ProvidersListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.provider_description.ProviderDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvidersListType) -> list:
    import aws_sdk_cognito_identity_provider.types.provider_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.provider_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvidersListType:
    import aws_sdk_cognito_identity_provider.types.provider_description

    out: ProvidersListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.provider_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
