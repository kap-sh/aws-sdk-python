"""Generated from Smithy shape ``com.amazonaws.appflow#OAuth2Defaults``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.auth_code_url_list
    import aws_sdk_appflow.types.o_auth2_custom_properties_list
    import aws_sdk_appflow.types.o_auth2_grant_type_supported_list
    import aws_sdk_appflow.types.o_auth_scope_list
    import aws_sdk_appflow.types.token_url_list


class OAuth2Defaults(TypedDict):
    oauth_scopes: NotRequired["aws_sdk_appflow.types.o_auth_scope_list.OAuthScopeList"]
    """<p>OAuth 2.0 scopes that the connector supports.</p>"""
    token_urls: NotRequired["aws_sdk_appflow.types.token_url_list.TokenUrlList"]
    """<p>Token URLs that can be used for OAuth 2.0 authentication.</p>"""
    auth_code_urls: NotRequired[
        "aws_sdk_appflow.types.auth_code_url_list.AuthCodeUrlList"
    ]
    """<p>Auth code URLs that can be used for OAuth 2.0 authentication.</p>"""
    oauth2_grant_types_supported: NotRequired[
        "aws_sdk_appflow.types.o_auth2_grant_type_supported_list.OAuth2GrantTypeSupportedList"
    ]
    """<p>OAuth 2.0 grant types supported by the connector.</p>"""
    oauth2_custom_properties: NotRequired[
        "aws_sdk_appflow.types.o_auth2_custom_properties_list.OAuth2CustomPropertiesList"
    ]
    """<p>List of custom parameters required for OAuth 2.0 authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OAuth2Defaults) -> dict:
    out: dict = {}
    if "oauth_scopes" in value:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["oauthScopes"] = aws_sdk_appflow.types.o_auth_scope_list.serialize_json(
            value["oauth_scopes"]
        )
    if "token_urls" in value:
        import aws_sdk_appflow.types.token_url_list

        out["tokenUrls"] = aws_sdk_appflow.types.token_url_list.serialize_json(
            value["token_urls"]
        )
    if "auth_code_urls" in value:
        import aws_sdk_appflow.types.auth_code_url_list

        out["authCodeUrls"] = aws_sdk_appflow.types.auth_code_url_list.serialize_json(
            value["auth_code_urls"]
        )
    if "oauth2_grant_types_supported" in value:
        import aws_sdk_appflow.types.o_auth2_grant_type_supported_list

        out["oauth2GrantTypesSupported"] = (
            aws_sdk_appflow.types.o_auth2_grant_type_supported_list.serialize_json(
                value["oauth2_grant_types_supported"]
            )
        )
    if "oauth2_custom_properties" in value:
        import aws_sdk_appflow.types.o_auth2_custom_properties_list

        out["oauth2CustomProperties"] = (
            aws_sdk_appflow.types.o_auth2_custom_properties_list.serialize_json(
                value["oauth2_custom_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> OAuth2Defaults:
    out: OAuth2Defaults = {}  # type: ignore[typeddict-item]
    if "oauthScopes" in data:
        import aws_sdk_appflow.types.o_auth_scope_list

        out["oauth_scopes"] = aws_sdk_appflow.types.o_auth_scope_list.deserialize_json(
            data["oauthScopes"]
        )
    if "tokenUrls" in data:
        import aws_sdk_appflow.types.token_url_list

        out["token_urls"] = aws_sdk_appflow.types.token_url_list.deserialize_json(
            data["tokenUrls"]
        )
    if "authCodeUrls" in data:
        import aws_sdk_appflow.types.auth_code_url_list

        out["auth_code_urls"] = (
            aws_sdk_appflow.types.auth_code_url_list.deserialize_json(
                data["authCodeUrls"]
            )
        )
    if "oauth2GrantTypesSupported" in data:
        import aws_sdk_appflow.types.o_auth2_grant_type_supported_list

        out["oauth2_grant_types_supported"] = (
            aws_sdk_appflow.types.o_auth2_grant_type_supported_list.deserialize_json(
                data["oauth2GrantTypesSupported"]
            )
        )
    if "oauth2CustomProperties" in data:
        import aws_sdk_appflow.types.o_auth2_custom_properties_list

        out["oauth2_custom_properties"] = (
            aws_sdk_appflow.types.o_auth2_custom_properties_list.deserialize_json(
                data["oauth2CustomProperties"]
            )
        )
    return out
