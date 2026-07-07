"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateResourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.resource_server_identifier_type
    import aws_sdk_cognito_identity_provider.types.resource_server_name_type
    import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type
    import aws_sdk_cognito_identity_provider.types.user_pool_id_type


class CreateResourceServerRequest(TypedDict, closed=True):
    user_pool_id: (
        "aws_sdk_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool where you want to create a resource server.</p>"""
    identifier: "aws_sdk_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
    """<p>A unique resource server identifier for the resource server. The identifier can be an API friendly name like <code>solar-system-data</code>. You can also set an API URL like <code>https://solar-system-data-api.example.com</code> as your identifier.</p> <p>Amazon Cognito represents scopes in the access token in the format <code>$resource-server-identifier/$scope</code>. Longer scope-identifier strings increase the size of your access tokens.</p>"""
    name: "aws_sdk_cognito_identity_provider.types.resource_server_name_type.ResourceServerNameType"
    """<p>A friendly name for the resource server.</p>"""
    scopes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.ResourceServerScopeListType"
    ]
    """<p>A list of custom scopes. Each scope is a key-value map with the keys <code>ScopeName</code> and <code>ScopeDescription</code>. The name of a custom scope is a combination of <code>ScopeName</code> and the resource server <code>Name</code> in this request, for example <code>MyResourceServerName/MyScopeName</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateResourceServerRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Identifier"] = value["identifier"]
    out["Name"] = value["name"]
    if "scopes" in value:
        import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type

        out["Scopes"] = (
            aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateResourceServerRequest:
    out: CreateResourceServerRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("CreateResourceServerRequest.user_pool_id required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("CreateResourceServerRequest.identifier required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateResourceServerRequest.name required")
    if "Scopes" in data:
        import aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type

        out["scopes"] = (
            aws_sdk_cognito_identity_provider.types.resource_server_scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
