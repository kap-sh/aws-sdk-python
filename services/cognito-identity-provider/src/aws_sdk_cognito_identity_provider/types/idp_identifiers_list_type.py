"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#IdpIdentifiersListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.idp_identifier_type

IdpIdentifiersListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.idp_identifier_type.IdpIdentifierType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IdpIdentifiersListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IdpIdentifiersListType:
    return list(data)
