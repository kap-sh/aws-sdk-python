"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#RoleMappingMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_identity.types.identity_provider_name
    import capo_cognito_identity.types.role_mapping

RoleMappingMap: TypeAlias = dict[
    "capo_cognito_identity.types.identity_provider_name.IdentityProviderName",
    "capo_cognito_identity.types.role_mapping.RoleMapping",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: RoleMappingMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_cognito_identity.types.role_mapping

        out[key] = capo_cognito_identity.types.role_mapping.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RoleMappingMap:
    out: RoleMappingMap = {}
    for key, value in data.items():
        import capo_cognito_identity.types.role_mapping

        out[key] = capo_cognito_identity.types.role_mapping.deserialize_aws_json_1_1(
            value
        )
    return out
