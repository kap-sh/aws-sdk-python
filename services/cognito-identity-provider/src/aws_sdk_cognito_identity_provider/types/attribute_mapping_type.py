"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AttributeMappingType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.attribute_mapping_key_type
    import aws_sdk_cognito_identity_provider.types.string_type

AttributeMappingType: TypeAlias = dict[
    "aws_sdk_cognito_identity_provider.types.attribute_mapping_key_type.AttributeMappingKeyType",
    "aws_sdk_cognito_identity_provider.types.string_type.StringType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AttributeMappingType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AttributeMappingType:
    out: AttributeMappingType = {}
    for key, value in data.items():
        out[key] = value
    return out
