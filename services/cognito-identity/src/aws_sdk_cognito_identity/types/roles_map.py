"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RolesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.arn_string
    import aws_sdk_cognito_identity.types.role_type

RolesMap: TypeAlias = dict[
    "aws_sdk_cognito_identity.types.role_type.RoleType",
    "aws_sdk_cognito_identity.types.arn_string.ARNString",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RolesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> RolesMap:
    out: RolesMap = {}
    for key, value in data.items():
        out[key] = value
    return out
