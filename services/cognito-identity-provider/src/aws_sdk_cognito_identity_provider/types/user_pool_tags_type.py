"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UserPoolTagsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.tag_keys_type
    import aws_sdk_cognito_identity_provider.types.tag_value_type

UserPoolTagsType: TypeAlias = dict[
    "aws_sdk_cognito_identity_provider.types.tag_keys_type.TagKeysType",
    "aws_sdk_cognito_identity_provider.types.tag_value_type.TagValueType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: UserPoolTagsType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> UserPoolTagsType:
    out: UserPoolTagsType = {}
    for key, value in data.items():
        out[key] = value
    return out
