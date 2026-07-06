"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateOAuthClientApplicationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.data_source_type
    import aws_sdk_quicksight.types.o_auth_authorization_endpoint_url
    import aws_sdk_quicksight.types.o_auth_client_application_id
    import aws_sdk_quicksight.types.o_auth_client_id
    import aws_sdk_quicksight.types.o_auth_client_secret
    import aws_sdk_quicksight.types.o_auth_scopes_string
    import aws_sdk_quicksight.types.o_auth_token_endpoint_url
    import aws_sdk_quicksight.types.resource_name
    import aws_sdk_quicksight.types.vpc_connection_properties


class UpdateOAuthClientApplicationRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    o_auth_client_application_id: (
        "aws_sdk_quicksight.types.o_auth_client_application_id.OAuthClientApplicationId"
    )
    """<p>The ID of the OAuthClientApplication that you want to update.</p>"""
    name: "aws_sdk_quicksight.types.resource_name.ResourceName"
    """<p>The display name for the OAuthClientApplication.</p>"""
    client_id: NotRequired["aws_sdk_quicksight.types.o_auth_client_id.OAuthClientId"]
    """<p>The client ID of the OAuth application that is registered with the identity provider.</p>"""
    client_secret: NotRequired[
        "aws_sdk_quicksight.types.o_auth_client_secret.OAuthClientSecret"
    ]
    """<p>The client secret of the OAuth application that is registered with the identity provider.</p>"""
    o_auth_token_endpoint_url: NotRequired[
        "aws_sdk_quicksight.types.o_auth_token_endpoint_url.OAuthTokenEndpointUrl"
    ]
    """<p>The token endpoint URL of the identity provider that is used to obtain access tokens.</p>"""
    o_auth_authorization_endpoint_url: NotRequired[
        "aws_sdk_quicksight.types.o_auth_authorization_endpoint_url.OAuthAuthorizationEndpointUrl"
    ]
    """<p>The authorization endpoint URL of the identity provider that is used to obtain authorization codes.</p>"""
    o_auth_scopes: NotRequired[
        "aws_sdk_quicksight.types.o_auth_scopes_string.OAuthScopesString"
    ]
    """<p>The OAuth scopes that are requested when the OAuthClientApplication obtains an access token from the identity provider.</p>"""
    data_source_type: NotRequired[
        "aws_sdk_quicksight.types.data_source_type.DataSourceType"
    ]
    """<p>The type of data source that the OAuthClientApplication is used with. Valid values are <code>SNOWFLAKE</code>.</p>"""
    identity_provider_vpc_connection_properties: NotRequired[
        "aws_sdk_quicksight.types.vpc_connection_properties.VpcConnectionProperties"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateOAuthClientApplicationRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "client_id" in value:
        out["ClientId"] = value["client_id"]
    if "client_secret" in value:
        out["ClientSecret"] = value["client_secret"]
    if "o_auth_token_endpoint_url" in value:
        out["OAuthTokenEndpointUrl"] = value["o_auth_token_endpoint_url"]
    if "o_auth_authorization_endpoint_url" in value:
        out["OAuthAuthorizationEndpointUrl"] = value[
            "o_auth_authorization_endpoint_url"
        ]
    if "o_auth_scopes" in value:
        out["OAuthScopes"] = value["o_auth_scopes"]
    if "data_source_type" in value:
        import aws_sdk_quicksight.types.data_source_type

        out["DataSourceType"] = (
            aws_sdk_quicksight.types.data_source_type.serialize_json(
                value["data_source_type"]
            )
        )
    if "identity_provider_vpc_connection_properties" in value:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["IdentityProviderVpcConnectionProperties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.serialize_json(
                value["identity_provider_vpc_connection_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateOAuthClientApplicationRequest:
    out: UpdateOAuthClientApplicationRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateOAuthClientApplicationRequest.name required")
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    if "OAuthTokenEndpointUrl" in data:
        out["o_auth_token_endpoint_url"] = data["OAuthTokenEndpointUrl"]
    if "OAuthAuthorizationEndpointUrl" in data:
        out["o_auth_authorization_endpoint_url"] = data["OAuthAuthorizationEndpointUrl"]
    if "OAuthScopes" in data:
        out["o_auth_scopes"] = data["OAuthScopes"]
    if "DataSourceType" in data:
        import aws_sdk_quicksight.types.data_source_type

        out["data_source_type"] = (
            aws_sdk_quicksight.types.data_source_type.deserialize_json(
                data["DataSourceType"]
            )
        )
    if "IdentityProviderVpcConnectionProperties" in data:
        import aws_sdk_quicksight.types.vpc_connection_properties

        out["identity_provider_vpc_connection_properties"] = (
            aws_sdk_quicksight.types.vpc_connection_properties.deserialize_json(
                data["IdentityProviderVpcConnectionProperties"]
            )
        )
    return out
