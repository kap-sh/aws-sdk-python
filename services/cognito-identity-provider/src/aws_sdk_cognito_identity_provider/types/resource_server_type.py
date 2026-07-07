"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ResourceServerType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.resource_server_identifier_type
    import aws_sdk_cognito_identity_provider.types.resource_server_name_type
    import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class ResourceServerType(TypedDict, closed=True):
    user_pool_id: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    ]
    """<p>The ID of the user pool that contains the resource server configuration.</p>"""
    identifier: NotRequired[
        "aws_sdk_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
    ]
    """<p>A unique resource server identifier for the resource server. The identifier can be an API friendly name like <code>solar-system-data</code>. You can also set an API URL like <code>https://solar-system-data-api.example.com</code> as your identifier.</p> <p>Amazon Cognito represents scopes in the access token in the format <code>$resource-server-identifier/$scope</code>. Longer scope-identifier strings increase the size of your access tokens.</p>"""
    name: NotRequired[
        "aws_sdk_cognito_identity_provider.types.resource_server_name_type.ResourceServerNameType"
    ]
    """<p>The name of the resource server.</p>"""
    scopes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.ResourceServerScopeListType"
    ]
    """<p>A list of scopes that are defined for the resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceServerType) -> dict:
    out: dict = {}
    if "user_pool_id" in value:
        out["UserPoolId"] = value["user_pool_id"]
    if "identifier" in value:
        out["Identifier"] = value["identifier"]
    if "name" in value:
        out["Name"] = value["name"]
    if "scopes" in value:
        import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type

        out["Scopes"] = (
            aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ResourceServerType:
    out: ResourceServerType = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Scopes" in data:
        import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type

        out["scopes"] = (
            aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
