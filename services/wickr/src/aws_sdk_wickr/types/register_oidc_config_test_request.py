"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOidcConfigTestRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class RegisterOidcConfigTestRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which the OIDC configuration will be tested.</p>"""
    extra_auth_params: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>Additional authentication parameters to include in the test (optional).</p>"""
    issuer: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The issuer URL of the OIDC provider to test.</p>"""
    scopes: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The OAuth scopes to test with the OIDC provider.</p>"""
    certificate: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The CA certificate for secure communication with the OIDC provider (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOidcConfigTestRequest) -> dict:
    out: dict = {}
    if "extra_auth_params" in value:
        out["extraAuthParams"] = value["extra_auth_params"]
    out["issuer"] = value["issuer"]
    out["scopes"] = value["scopes"]
    if "certificate" in value:
        out["certificate"] = value["certificate"]
    return out


def deserialize_json(data: dict) -> RegisterOidcConfigTestRequest:
    out: RegisterOidcConfigTestRequest = {}  # type: ignore[typeddict-item]
    if "extraAuthParams" in data:
        out["extra_auth_params"] = data["extraAuthParams"]
    if "issuer" in data:
        out["issuer"] = data["issuer"]
    else:
        raise DeserializationError("RegisterOidcConfigTestRequest.issuer required")
    if "scopes" in data:
        out["scopes"] = data["scopes"]
    else:
        raise DeserializationError("RegisterOidcConfigTestRequest.scopes required")
    if "certificate" in data:
        out["certificate"] = data["certificate"]
    return out
