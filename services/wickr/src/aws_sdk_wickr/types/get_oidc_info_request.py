"""Generated from Smithy shape ``com.amazonaws.wickr#GetOidcInfoRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sensitive_string


class GetOidcInfoRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network whose OIDC configuration will be retrieved.</p>"""
    client_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OAuth client ID for retrieving access tokens (optional).</p>"""
    code: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The authorization code for retrieving access tokens (optional).</p>"""
    grant_type: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The OAuth grant type for retrieving access tokens (optional).</p>"""
    redirect_uri: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The redirect URI for the OAuth flow (optional).</p>"""
    url: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The URL for the OIDC provider (optional).</p>"""
    client_secret: NotRequired["aws_sdk_wickr.types.sensitive_string.SensitiveString"]
    """<p>The OAuth client secret for retrieving access tokens (optional).</p>"""
    code_verifier: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The PKCE code verifier for enhanced security in the OAuth flow (optional).</p>"""
    certificate: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The CA certificate for secure communication with the OIDC provider (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOidcInfoRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetOidcInfoRequest:
    out: GetOidcInfoRequest = {}  # type: ignore[typeddict-item]
    return out
