"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.user_pool_description_type

UserPoolListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.user_pool_description_type.UserPoolDescriptionType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserPoolListType) -> list:
    import aws_sdk_cognito_identity_provider.types.user_pool_description_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.user_pool_description_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UserPoolListType:
    import aws_sdk_cognito_identity_provider.types.user_pool_description_type

    out: UserPoolListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.user_pool_description_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
