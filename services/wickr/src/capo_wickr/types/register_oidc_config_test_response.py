"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOidcConfigTestResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.string_list


class RegisterOidcConfigTestResponse(TypedDict, closed=True):
    token_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token endpoint URL discovered from the OIDC provider.</p>"""
    userinfo_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The user info endpoint URL discovered from the OIDC provider.</p>"""
    response_types_supported: NotRequired["capo_wickr.types.string_list.StringList"]
    """<p>The OAuth response types supported by the OIDC provider.</p>"""
    scopes_supported: NotRequired["capo_wickr.types.string_list.StringList"]
    """<p>The OAuth scopes supported by the OIDC provider.</p>"""
    issuer: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The issuer URL confirmed by the OIDC provider.</p>"""
    authorization_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The authorization endpoint URL discovered from the OIDC provider.</p>"""
    end_session_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The end session endpoint URL for logging out users from the OIDC provider.</p>"""
    logout_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The logout endpoint URL for terminating user sessions.</p>"""
    grant_types_supported: NotRequired["capo_wickr.types.string_list.StringList"]
    """<p>The OAuth grant types supported by the OIDC provider.</p>"""
    revocation_endpoint: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The token revocation endpoint URL for invalidating tokens.</p>"""
    token_endpoint_auth_methods_supported: NotRequired[
        "capo_wickr.types.string_list.StringList"
    ]
    """<p>The authentication methods supported by the token endpoint.</p>"""
    microsoft_multi_refresh_token: NotRequired["bool"]
    """<p>Indicates whether the provider supports Microsoft multi-refresh tokens.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOidcConfigTestResponse) -> dict:
    out: dict = {}
    if "token_endpoint" in value:
        out["tokenEndpoint"] = value["token_endpoint"]
    if "userinfo_endpoint" in value:
        out["userinfoEndpoint"] = value["userinfo_endpoint"]
    if "response_types_supported" in value:
        import capo_wickr.types.string_list

        out["responseTypesSupported"] = capo_wickr.types.string_list.serialize_json(
            value["response_types_supported"]
        )
    if "scopes_supported" in value:
        import capo_wickr.types.string_list

        out["scopesSupported"] = capo_wickr.types.string_list.serialize_json(
            value["scopes_supported"]
        )
    if "issuer" in value:
        out["issuer"] = value["issuer"]
    if "authorization_endpoint" in value:
        out["authorizationEndpoint"] = value["authorization_endpoint"]
    if "end_session_endpoint" in value:
        out["endSessionEndpoint"] = value["end_session_endpoint"]
    if "logout_endpoint" in value:
        out["logoutEndpoint"] = value["logout_endpoint"]
    if "grant_types_supported" in value:
        import capo_wickr.types.string_list

        out["grantTypesSupported"] = capo_wickr.types.string_list.serialize_json(
            value["grant_types_supported"]
        )
    if "revocation_endpoint" in value:
        out["revocationEndpoint"] = value["revocation_endpoint"]
    if "token_endpoint_auth_methods_supported" in value:
        import capo_wickr.types.string_list

        out["tokenEndpointAuthMethodsSupported"] = (
            capo_wickr.types.string_list.serialize_json(
                value["token_endpoint_auth_methods_supported"]
            )
        )
    if "microsoft_multi_refresh_token" in value:
        out["microsoftMultiRefreshToken"] = value["microsoft_multi_refresh_token"]
    return out


def deserialize_json(data: dict) -> RegisterOidcConfigTestResponse:
    out: RegisterOidcConfigTestResponse = {}  # type: ignore[typeddict-item]
    if "tokenEndpoint" in data:
        out["token_endpoint"] = data["tokenEndpoint"]
    if "userinfoEndpoint" in data:
        out["userinfo_endpoint"] = data["userinfoEndpoint"]
    if "responseTypesSupported" in data:
        import capo_wickr.types.string_list

        out["response_types_supported"] = capo_wickr.types.string_list.deserialize_json(
            data["responseTypesSupported"]
        )
    if "scopesSupported" in data:
        import capo_wickr.types.string_list

        out["scopes_supported"] = capo_wickr.types.string_list.deserialize_json(
            data["scopesSupported"]
        )
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    if "authorizationEndpoint" in data:
        out["authorization_endpoint"] = data["authorizationEndpoint"]
    if "endSessionEndpoint" in data:
        out["end_session_endpoint"] = data["endSessionEndpoint"]
    if "logoutEndpoint" in data:
        out["logout_endpoint"] = data["logoutEndpoint"]
    if "grantTypesSupported" in data:
        import capo_wickr.types.string_list

        out["grant_types_supported"] = capo_wickr.types.string_list.deserialize_json(
            data["grantTypesSupported"]
        )
    if "revocationEndpoint" in data:
        out["revocation_endpoint"] = data["revocationEndpoint"]
    if "tokenEndpointAuthMethodsSupported" in data:
        import capo_wickr.types.string_list

        out["token_endpoint_auth_methods_supported"] = (
            capo_wickr.types.string_list.deserialize_json(
                data["tokenEndpointAuthMethodsSupported"]
            )
        )
    if "microsoftMultiRefreshToken" in data:
        out["microsoft_multi_refresh_token"] = data["microsoftMultiRefreshToken"]
    return out
