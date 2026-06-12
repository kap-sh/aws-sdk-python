"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ClientMetadataType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.string_type

ClientMetadataType: TypeAlias = dict[
    "aws_sdk_cognito_identity_provider.types.string_type.StringType",
    "aws_sdk_cognito_identity_provider.types.string_type.StringType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ClientMetadataType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ClientMetadataType:
    out: ClientMetadataType = {}
    for key, value in data.items():
        out[key] = value
    return out
