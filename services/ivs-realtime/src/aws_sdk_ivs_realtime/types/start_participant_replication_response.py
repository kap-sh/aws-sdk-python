"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StartParticipantReplicationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.string


class StartParticipantReplicationResponse(TypedDict):
    access_control_allow_origin: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin\">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired[
        "aws_sdk_ivs_realtime.types.string.String"
    ]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers\">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    cache_control: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control\">Cache-Control</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy\">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security\">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""
    x_content_type_options: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options\">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    x_frame_options: NotRequired["aws_sdk_ivs_realtime.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options\">X-Frame-Options</a> in the MDN Web Docs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartParticipantReplicationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StartParticipantReplicationResponse:
    out: StartParticipantReplicationResponse = {}  # type: ignore[typeddict-item]
    return out
