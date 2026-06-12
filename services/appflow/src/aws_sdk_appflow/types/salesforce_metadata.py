"""Generated from Smithy shape ``com.amazonaws.appflow#SalesforceMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.o_auth2_grant_type_supported_list
    import aws_sdk_appflow.types.o_auth_scope_list
    import aws_sdk_appflow.types.salesforce_data_transfer_api_list


class SalesforceMetadata(TypedDict):
    o_auth_scopes: NotRequired["aws_sdk_appflow.types.o_auth_scope_list.OAuthScopeList"]
    """<p> The desired authorization scope for the Salesforce account. </p>"""
    data_transfer_apis: NotRequired[
        "aws_sdk_appflow.types.salesforce_data_transfer_api_list.SalesforceDataTransferApiList"
    ]
    """<p>The Salesforce APIs that you can have Amazon AppFlow use when your flows transfers data to or from Salesforce.</p>"""
    oauth2_grant_types_supported: NotRequired[
        "aws_sdk_appflow.types.o_auth2_grant_type_supported_list.OAuth2GrantTypeSupportedList"
    ]
    """<p>The OAuth 2.0 grant types that Amazon AppFlow can use when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.</p> <dl> <dt>AUTHORIZATION_CODE</dt> <dd> <p>Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.</p> </dd> <dt>JWT_BEARER</dt> <dd> <p>Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.</p> </dd> </dl> <note> <p>The CLIENT_CREDENTIALS value is not supported for Salesforce.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: SalesforceMetadata) -> dict:
    out: dict = {}
    if "o_auth_scopes" in value:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["oAuthScopes"] = aws_sdk_appflow.types.o_auth_scope_list.serialize_json(
            value["o_auth_scopes"]
        )
    if "data_transfer_apis" in value:
        import aws_sdk_appflow.types.salesforce_data_transfer_api_list

        out["dataTransferApis"] = (
            aws_sdk_appflow.types.salesforce_data_transfer_api_list.serialize_json(
                value["data_transfer_apis"]
            )
        )
    if "oauth2_grant_types_supported" in value:
        import aws_sdk_appflow.types.o_auth2_grant_type_supported_list

        out["oauth2GrantTypesSupported"] = (
            aws_sdk_appflow.types.o_auth2_grant_type_supported_list.serialize_json(
                value["oauth2_grant_types_supported"]
            )
        )
    return out


def deserialize_json(data: dict) -> SalesforceMetadata:
    out: SalesforceMetadata = {}  # type: ignore[typeddict-item]
    if "oAuthScopes" in data:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["o_auth_scopes"] = aws_sdk_appflow.types.o_auth_scope_list.deserialize_json(
            data["oAuthScopes"]
        )
    if "dataTransferApis" in data:
        import aws_sdk_appflow.types.salesforce_data_transfer_api_list

        out["data_transfer_apis"] = (
            aws_sdk_appflow.types.salesforce_data_transfer_api_list.deserialize_json(
                data["dataTransferApis"]
            )
        )
    if "oauth2GrantTypesSupported" in data:
        import aws_sdk_appflow.types.o_auth2_grant_type_supported_list

        out["oauth2_grant_types_supported"] = (
            aws_sdk_appflow.types.o_auth2_grant_type_supported_list.deserialize_json(
                data["oauth2GrantTypesSupported"]
            )
        )
    return out
