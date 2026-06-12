"""Generated from Smithy shape ``com.amazonaws.ivs#BatchGetChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.batch_errors
    import aws_sdk_ivs.types.channels
    import aws_sdk_ivs.types.string


class BatchGetChannelResponse(TypedDict):
    access_control_allow_origin: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin\">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers\">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    cache_control: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control\">Cache-Control</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy\">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security\">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""
    x_content_type_options: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options\">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    x_frame_options: NotRequired["aws_sdk_ivs.types.string.String"]
    """<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options\">X-Frame-Options</a> in the MDN Web Docs.</p>"""
    channels: NotRequired["aws_sdk_ivs.types.channels.Channels"]
    """<p/>"""
    errors: NotRequired["aws_sdk_ivs.types.batch_errors.BatchErrors"]
    """<p>Each error object is related to a specific ARN in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetChannelResponse) -> dict:
    out: dict = {}
    if "channels" in value:
        import aws_sdk_ivs.types.channels

        out["channels"] = aws_sdk_ivs.types.channels.serialize_json(value["channels"])
    if "errors" in value:
        import aws_sdk_ivs.types.batch_errors

        out["errors"] = aws_sdk_ivs.types.batch_errors.serialize_json(value["errors"])
    return out


def deserialize_json(data: dict) -> BatchGetChannelResponse:
    out: BatchGetChannelResponse = {}  # type: ignore[typeddict-item]
    if "channels" in data:
        import aws_sdk_ivs.types.channels

        out["channels"] = aws_sdk_ivs.types.channels.deserialize_json(data["channels"])
    if "errors" in data:
        import aws_sdk_ivs.types.batch_errors

        out["errors"] = aws_sdk_ivs.types.batch_errors.deserialize_json(data["errors"])
    return out
