"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientSecretDescriptorListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type

ClientSecretDescriptorListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.ClientSecretDescriptorType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientSecretDescriptorListType) -> list:
    import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ClientSecretDescriptorListType:
    import aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type

    out: ClientSecretDescriptorListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.client_secret_descriptor_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
