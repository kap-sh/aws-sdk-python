"""Generated from Smithy shape ``com.amazonaws.cognitoidentity#GetIdentityPoolRolesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity.types.identity_pool_id
    import aws_sdk_cognito_identity.types.role_mapping_map
    import aws_sdk_cognito_identity.types.roles_map


class GetIdentityPoolRolesResponse(TypedDict, closed=True):
    identity_pool_id: NotRequired[
        "aws_sdk_cognito_identity.types.identity_pool_id.IdentityPoolId"
    ]
    """<p>An identity pool ID in the format REGION:GUID.</p>"""
    roles: NotRequired["aws_sdk_cognito_identity.types.roles_map.RolesMap"]
    """<p>The map of roles associated with this pool. Currently only authenticated and unauthenticated roles are supported.</p>"""
    role_mappings: NotRequired[
        "aws_sdk_cognito_identity.types.role_mapping_map.RoleMappingMap"
    ]
    """<p>How users for a specific identity provider are to mapped to roles. This is a String-to-<a>RoleMapping</a> object map. The string identifies the identity provider, for example, <code>graph.facebook.com</code> or <code>cognito-idp.us-east-1.amazonaws.com/us-east-1_abcdefghi:app_client_id</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetIdentityPoolRolesResponse) -> dict:
    out: dict = {}
    if "identity_pool_id" in value:
        out["IdentityPoolId"] = value["identity_pool_id"]
    if "roles" in value:
        import aws_sdk_cognito_identity.types.roles_map

        out["Roles"] = aws_sdk_cognito_identity.types.roles_map.serialize_aws_json_1_1(
            value["roles"]
        )
    if "role_mappings" in value:
        import aws_sdk_cognito_identity.types.role_mapping_map

        out["RoleMappings"] = (
            aws_sdk_cognito_identity.types.role_mapping_map.serialize_aws_json_1_1(
                value["role_mappings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetIdentityPoolRolesResponse:
    out: GetIdentityPoolRolesResponse = {}  # type: ignore[typeddict-item]
    if "IdentityPoolId" in data:
        out["identity_pool_id"] = data["IdentityPoolId"]
    if "Roles" in data:
        import aws_sdk_cognito_identity.types.roles_map

        out["roles"] = (
            aws_sdk_cognito_identity.types.roles_map.deserialize_aws_json_1_1(
                data["Roles"]
            )
        )
    if "RoleMappings" in data:
        import aws_sdk_cognito_identity.types.role_mapping_map

        out["role_mappings"] = (
            aws_sdk_cognito_identity.types.role_mapping_map.deserialize_aws_json_1_1(
                data["RoleMappings"]
            )
        )
    return out
