"""Generated from Smithy shape ``com.amazonaws.wickr#GetOpentdfConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_wickr.types.generic_string
    import capo_wickr.types.sensitive_string


class GetOpentdfConfigResponse(TypedDict, closed=True):
    client_id: "capo_wickr.types.generic_string.GenericString"
    """<p>The OIDC client ID used for authenticating with the OpenTDF provider.</p>"""
    domain: "capo_wickr.types.generic_string.GenericString"
    """<p>The domain of the OpenTDF server.</p>"""
    client_secret: "capo_wickr.types.sensitive_string.SensitiveString"
    """<p>The OIDC client secret used for authenticating with the OpenTDF provider.</p>"""
    provider: "capo_wickr.types.generic_string.GenericString"
    """<p>The provider of the OpenTDF platform.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOpentdfConfigResponse) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["domain"] = value["domain"]
    out["clientSecret"] = value["client_secret"]
    out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> GetOpentdfConfigResponse:
    out: GetOpentdfConfigResponse = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("GetOpentdfConfigResponse.client_id required")
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("GetOpentdfConfigResponse.domain required")
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError("GetOpentdfConfigResponse.client_secret required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("GetOpentdfConfigResponse.provider required")
    return out
