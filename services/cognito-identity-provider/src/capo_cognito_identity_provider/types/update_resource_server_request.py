"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#UpdateResourceServerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.resource_server_identifier_type
    import capo_cognito_identity_provider.types.resource_server_name_type
    import capo_cognito_identity_provider.types.resource_server_scope_list_type
    import capo_cognito_identity_provider.types.user_pool_id_type


class UpdateResourceServerRequest(TypedDict, closed=True):
    user_pool_id: (
        "capo_cognito_identity_provider.types.user_pool_id_type.UserPoolIdType"
    )
    """<p>The ID of the user pool that contains the resource server that you want to update.</p>"""
    identifier: "capo_cognito_identity_provider.types.resource_server_identifier_type.ResourceServerIdentifierType"
    """<p>A unique resource server identifier for the resource server. The identifier can be an API friendly name like <code>solar-system-data</code>. You can also set an API URL like <code>https://solar-system-data-api.example.com</code> as your identifier.</p> <p>Amazon Cognito represents scopes in the access token in the format <code>$resource-server-identifier/$scope</code>. Longer scope-identifier strings increase the size of your access tokens.</p>"""
    name: "capo_cognito_identity_provider.types.resource_server_name_type.ResourceServerNameType"
    """<p>The updated name of the resource server.</p>"""
    scopes: NotRequired[
        "capo_cognito_identity_provider.types.resource_server_scope_list_type.ResourceServerScopeListType"
    ]
    """<p>An array of updated custom scope names and descriptions that you want to associate with your resource server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateResourceServerRequest) -> dict:
    out: dict = {}
    out["UserPoolId"] = value["user_pool_id"]
    out["Identifier"] = value["identifier"]
    out["Name"] = value["name"]
    if "scopes" in value:
        import capo_cognito_identity_provider.types.resource_server_scope_list_type

        out["Scopes"] = (
            capo_cognito_identity_provider.types.resource_server_scope_list_type.serialize_aws_json_1_1(
                value["scopes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateResourceServerRequest:
    out: UpdateResourceServerRequest = {}  # type: ignore[typeddict-item]
    if "UserPoolId" in data:
        out["user_pool_id"] = data["UserPoolId"]
    else:
        raise DeserializationError("UpdateResourceServerRequest.user_pool_id required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("UpdateResourceServerRequest.identifier required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateResourceServerRequest.name required")
    if "Scopes" in data:
        import capo_cognito_identity_provider.types.resource_server_scope_list_type

        out["scopes"] = (
            capo_cognito_identity_provider.types.resource_server_scope_list_type.deserialize_aws_json_1_1(
                data["Scopes"]
            )
        )
    return out
