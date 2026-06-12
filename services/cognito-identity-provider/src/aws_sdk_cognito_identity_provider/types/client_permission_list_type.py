"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientPermissionListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.client_permission_type

ClientPermissionListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.client_permission_type.ClientPermissionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClientPermissionListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ClientPermissionListType:
    return list(data)
