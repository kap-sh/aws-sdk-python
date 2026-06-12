"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RoleMappingMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_provider_name
    import aws_sdk_cognito_identity.types.role_mapping

RoleMappingMap: TypeAlias = dict[
    "aws_sdk_cognito_identity.types.identity_provider_name.IdentityProviderName",
    "aws_sdk_cognito_identity.types.role_mapping.RoleMapping",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RoleMappingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_cognito_identity.types.role_mapping

        out[key] = aws_sdk_cognito_identity.types.role_mapping.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoleMappingMap:
    out: RoleMappingMap = {}
    for key, value in data.items():
        import aws_sdk_cognito_identity.types.role_mapping

        out[key] = aws_sdk_cognito_identity.types.role_mapping.deserialize_aws_json_1_1(
            value
        )
    return out
