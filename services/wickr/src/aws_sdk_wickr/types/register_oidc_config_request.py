"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOidcConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sensitive_string


class RegisterOidcConfigRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which OIDC will be configured.</p>"""
    company_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>Custom identifier your end users will use to sign in with SSO.</p>"""
    custom_username: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A custom field mapping to extract the username from the OIDC token (optional). </p> <note> <p>The customUsername is only required if you use something other than email as the username field.</p> </note>"""
    extra_auth_params: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Additional authentication parameters to include in the OIDC flow (optional).</p>"""
    issuer: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The issuer URL of the OIDC provider (e.g., 'https://login.example.com').</p>"""
    scopes: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The OAuth scopes to request from the OIDC provider (e.g., 'openid profile email').</p>"""
    secret: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The client secret for authenticating with the OIDC provider (optional).</p>"""
    sso_token_buffer_minutes: NotRequired["int"]
    """<p>The buffer time in minutes before the SSO token expires to refresh it (optional).</p>"""
    user_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Unique identifier provided by your identity provider to authenticate the access request. Also referred to as clientID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOidcConfigRequest) -> dict:
    out: dict = {}
    out["companyId"] = value["company_id"]
    if "custom_username" in value:
        out["customUsername"] = value["custom_username"]
    if "extra_auth_params" in value:
        out["extraAuthParams"] = value["extra_auth_params"]
    out["issuer"] = value["issuer"]
    out["scopes"] = value["scopes"]
    if "secret" in value:
        out["secret"] = value["secret"]
    if "sso_token_buffer_minutes" in value:
        out["ssoTokenBufferMinutes"] = value["sso_token_buffer_minutes"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    return out


def deserialize_json(data: dict) -> RegisterOidcConfigRequest:
    out: RegisterOidcConfigRequest = {}  # type: ignore[typeddict-item]
    if "companyId" in data:
        out["company_id"] = data["companyId"]
    else:
        raise DeserializationError("RegisterOidcConfigRequest.company_id required")
    if "customUsername" in data:
        out["custom_username"] = data["customUsername"]
    if "extraAuthParams" in data:
        out["extra_auth_params"] = data["extraAuthParams"]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("RegisterOidcConfigRequest.issuer required")
    if "scopes" in data:
        out["scopes"] = data["scopes"]
    else:
        raise DeserializationError("RegisterOidcConfigRequest.scopes required")
    if "secret" in data:
        out["secret"] = data["secret"]
    if "ssoTokenBufferMinutes" in data:
        out["sso_token_buffer_minutes"] = data["ssoTokenBufferMinutes"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    return out
