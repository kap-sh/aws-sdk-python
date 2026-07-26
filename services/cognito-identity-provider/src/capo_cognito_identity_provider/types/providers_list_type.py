"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ProvidersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.provider_description

ProvidersListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.provider_description.ProviderDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvidersListType) -> list:
    import capo_cognito_identity_provider.types.provider_description

    out: list = []
    for item in value:
        out.append(
            capo_cognito_identity_provider.types.provider_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvidersListType:
    import capo_cognito_identity_provider.types.provider_description

    out: ProvidersListType = []
    for item in data:
        out.append(
            capo_cognito_identity_provider.types.provider_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
