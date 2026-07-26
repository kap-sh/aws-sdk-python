"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AuthParametersType``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.string_type

AuthParametersType: TypeAlias = dict[
    "capo_cognito_identity_provider.types.string_type.StringType",
    "capo_cognito_identity_provider.types.string_type.StringType",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: AuthParametersType) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> AuthParametersType:
    out: AuthParametersType = {}
    for key, value in data.items():
        out[key] = value
    return out
