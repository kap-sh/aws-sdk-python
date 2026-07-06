"""Generated from Smithy shape ``com.amazonaws.wickr#RegisterOpentdfConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_wickr.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id
    import aws_sdk_wickr.types.sensitive_string


class RegisterOpentdfConfigRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network for which OpenTDF integration will be configured.</p>"""
    client_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The OIDC client ID used for authenticating with the OpenTDF provider.</p>"""
    client_secret: "aws_sdk_wickr.types.sensitive_string.SensitiveString"
    """<p>The OIDC client secret used for authenticating with the OpenTDF provider</p>"""
    domain: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The domain of the OpenTDF server.</p>"""
    provider: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The provider of the OpenTDF platform.</p> <note> <p>Currently only Virtru is supported as the OpenTDF provider.</p> </note>"""
    dry_run: NotRequired["bool"]
    """<p>Perform dry-run test connection of OpenTDF configuration (optional).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterOpentdfConfigRequest) -> dict:
    out: dict = {}
    out["clientId"] = value["client_id"]
    out["clientSecret"] = value["client_secret"]
    out["domain"] = value["domain"]
    out["provider"] = value["provider"]
    return out


def deserialize_json(data: dict) -> RegisterOpentdfConfigRequest:
    out: RegisterOpentdfConfigRequest = {}  # type: ignore[typeddict-item]
    if "clientId" in data:
        out["client_id"] = data["clientId"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.client_id required")
    if "clientSecret" in data:
        out["client_secret"] = data["clientSecret"]
    else:
        raise DeserializationError(
            "RegisterOpentdfConfigRequest.client_secret required"
        )
    if "domain" in data:
        out["domain"] = data["domain"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.domain required")
    if "provider" in data:
        out["provider"] = data["provider"]
    else:
        raise DeserializationError("RegisterOpentdfConfigRequest.provider required")
    return out
