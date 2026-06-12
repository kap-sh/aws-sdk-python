"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolTagsListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.tag_keys_type

UserPoolTagsListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.tag_keys_type.TagKeysType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolTagsListType) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> UserPoolTagsListType:
    return list(data)
