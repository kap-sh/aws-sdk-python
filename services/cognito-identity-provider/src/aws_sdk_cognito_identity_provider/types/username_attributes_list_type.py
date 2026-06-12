"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UsernameAttributesListType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.username_attribute_type

UsernameAttributesListType: TypeAlias = list[
    "aws_sdk_cognito_identity_provider.types.username_attribute_type.UsernameAttributeType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UsernameAttributesListType) -> list:
    import aws_sdk_cognito_identity_provider.types.username_attribute_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cognito_identity_provider.types.username_attribute_type.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> UsernameAttributesListType:
    import aws_sdk_cognito_identity_provider.types.username_attribute_type

    out: UsernameAttributesListType = []
    for item in data:
        out.append(
            aws_sdk_cognito_identity_provider.types.username_attribute_type.deserialize_aws_json_1_1(
                item
            )
        )
    return out
