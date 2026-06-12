"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#IdentityPoolTagsType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.tag_keys_type
    import aws_sdk_cognito_identity.types.tag_value_type

IdentityPoolTagsType: TypeAlias = dict[
    "aws_sdk_cognito_identity.types.tag_keys_type.TagKeysType",
    "aws_sdk_cognito_identity.types.tag_value_type.TagValueType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: IdentityPoolTagsType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> IdentityPoolTagsType:
    out: IdentityPoolTagsType = {}
    for key, value in data.items():
        out[key] = value
    return out
