"""Generated from Smithy shape ``com.amazonaws.wickr#OidcConfigInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.sensitive_string


class OidcConfigInfo(TypedDict):
    application_name: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The name of the OIDC application as registered with the identity provider.</p>"""
    client_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OAuth client ID assigned by the identity provider for authentication requests.</p>"""
    company_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>Custom identifier your end users will use to sign in with SSO.</p>"""
    scopes: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The OAuth scopes requested from the identity provider, which determine what user information is accessible (e.g., 'openid profile email').</p>"""
    issuer: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The issuer URL of the identity provider, which serves as the base URL for OIDC endpoints and configuration discovery.</p>"""
    client_secret: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The OAuth client secret used to authenticate the application with the identity provider.</p>"""
    secret: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>An additional secret credential used by the identity provider for authentication.</p>"""
    redirect_url: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The callback URL where the identity provider redirects users after successful authentication. This URL must be registered with the identity provider.</p>"""
    user_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The claim field from the OIDC token to use as the unique user identifier (e.g., 'email', 'sub', or a custom claim).</p>"""
    custom_username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A custom field mapping to extract the username from the OIDC token when the standard username claim is insufficient.</p>"""
    ca_certificate: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The X.509 CA certificate for validating SSL/TLS connections to the identity provider when using self-signed or enterprise certificates.</p>"""
    application_id: NotRequired["int"]
    """<p>The unique identifier for the registered OIDC application. Valid range is 1-10.</p>"""
    sso_token_buffer_minutes: NotRequired["int"]
    """<p>The grace period in minutes before the SSO token expires when the system should proactively refresh the token to maintain seamless user access.</p>"""
    extra_auth_params: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Additional authentication parameters to include in the OIDC authorization request as a query string. Useful for provider-specific extensions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OidcConfigInfo) -> dict:
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


def deserialize_json(data: dict) -> OidcConfigInfo:
    out: OidcConfigInfo = {}  # type: ignore[typeddict-item]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    if "companyId" in data:
        out["company_id"] = data["companyId"]
    else:
        raise DeserializationError("OidcConfigInfo.company_id required")
    if "scopes" in data:
        out["scopes"] = data["scopes"]
    else:
        raise DeserializationError("OidcConfigInfo.scopes required")
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("OidcConfigInfo.issuer required")
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
