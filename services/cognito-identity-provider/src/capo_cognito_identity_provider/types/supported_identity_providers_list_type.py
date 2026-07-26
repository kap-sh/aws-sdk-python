"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SupportedIdentityProvidersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.provider_name_type

SupportedIdentityProvidersListType: TypeAlias = list[
    "capo_cognito_identity_provider.types.provider_name_type.ProviderNameType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SupportedIdentityProvidersListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> SupportedIdentityProvidersListType:
    return list(data)
