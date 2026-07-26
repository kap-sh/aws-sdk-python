"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOidcConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.sensitive_string


class RegisterOidcConfigResponse(TypedDict, closed=True):
    application_name: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The name of the registered OIDC application.</p>"""
    client_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The OAuth client ID assigned to the application.</p>"""
    company_id: "capo_wickr.types.generic_string.GenericString"
    """<p>Custom identifier your end users will use to sign in with SSO.</p>"""
    scopes: "capo_wickr.types.generic_string.GenericString"
    """<p>The OAuth scopes configured for the application.</p>"""
    issuer: "capo_wickr.types.generic_string.GenericString"
    """<p>The issuer URL of the OIDC provider.</p>"""
    client_secret: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The OAuth client secret for the application.</p>"""
    secret: NotRequired["capo_wickr.types.sensitive_string.SensitiveString"]
    """<p>The client secret for authenticating with the OIDC provider.</p>"""
    redirect_url: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The redirect URL configured for the OAuth flow.</p>"""
    user_id: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The claim field being used as the user identifier.</p>"""
    custom_username: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The custom field mapping used for extracting the username.</p>"""
    ca_certificate: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The CA certificate used for secure communication with the OIDC provider.</p>"""
    application_id: NotRequired["int"]
    """<p>The unique identifier for the registered OIDC application.</p>"""
    sso_token_buffer_minutes: NotRequired["int"]
    """<p>The buffer time in minutes before the SSO token expires.</p>"""
    extra_auth_params: NotRequired["capo_wickr.types.generic_string.GenericString"]
    """<p>The additional authentication parameters configured for the OIDC flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOidcConfigResponse) -> dict:
    out: dict = {}
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "client_id" in value:
        out["clientId"] = value["client_id"]
    out["companyId"] = value["company_id"]
    out["scopes"] = value["scopes"]
    out["issuer"] = value["issuer"]
    if "client_secret" in value:
        out["clientSecret"] = value["client_secret"]
    if "secret" in value:
        out["secret"] = value["secret"]
    if "redirect_url" in value:
        out["redirectUrl"] = value["redirect_url"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    if "custom_username" in value:
        out["customUsername"] = value["custom_username"]
    if "ca_certificate" in value:
        out["caCertificate"] = value["ca_certificate"]
    if "application_id" in value:
        out["applicationId"] = value["application_id"]
    if "sso_token_buffer_minutes" in value:
        out["ssoTokenBufferMinutes"] = value["sso_token_buffer_minutes"]
    if "extra_auth_params" in value:
        out["extraAuthParams"] = value["extra_auth_params"]
    return out


def deserialize_json(data: dict) -> RegisterOidcConfigResponse:
    out: RegisterOidcConfigResponse = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "companyId" in data:
        out["company_id"] = data["companyId"]
    else:
        raise DeserializationError("RegisterOidcConfigResponse.company_id required")
    if "scopes" in data:
        out["scopes"] = data["scopes"]
    else:
        raise DeserializationError("RegisterOidcConfigResponse.scopes required")
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("RegisterOidcConfigResponse.issuer required")
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    if "secret" in data:
        out["secret"] = data["secret"]
    if "redirectUrl" in data:
        out["redirect_url"] = data["redirectUrl"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "customUsername" in data:
        out["custom_username"] = data["customUsername"]
    if "caCertificate" in data:
        out["ca_certificate"] = data["caCertificate"]
    if "applicationId" in data:
        out["application_id"] = data["applicationId"]
    if "ssoTokenBufferMinutes" in data:
        out["sso_token_buffer_minutes"] = data["ssoTokenBufferMinutes"]
    if "extraAuthParams" in data:
        out["extra_auth_params"] = data["extraAuthParams"]
    return out
