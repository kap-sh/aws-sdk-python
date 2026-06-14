"""Generated from Smithy shape ``com.amazonaws.ivs#BatchStartViewerSessionRevocationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors
    import aws_sdk_ivs.types.string


class BatchStartViewerSessionRevocationResponse(TypedDict):
    access_control_allow_origin: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin\">Access-Control-Allow-Origin</a> in the MDN Web Docs.</p>"""
    access_control_expose_headers: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers\">Access-Control-Expose-Headers</a> in the MDN Web Docs.</p>"""
    cache_control: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control\">Cache-Control</a> in the MDN Web Docs.</p>"""
    content_security_policy: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy\">Content-Security-Policy</a> in the MDN Web Docs.</p>"""
    strict_transport_security: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security\">Strict-Transport-Security</a> in the MDN Web Docs.</p>"""
    x_content_type_options: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options\">X-Content-Type-Options</a> in the MDN Web Docs.</p>"""
    x_frame_options: NotRequired["aws_sdk_ivs.types.string.String"]
    r"""<p>See <a href=\"https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Frame-Options\">X-Frame-Options</a> in the MDN Web Docs.</p>"""
    errors: NotRequired[
        "aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors.BatchStartViewerSessionRevocationErrors"
    ]
    """<p>Each error object is related to a specific <code>channelArn</code> and <code>viewerId</code> pair in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchStartViewerSessionRevocationResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors

        out["errors"] = (
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchStartViewerSessionRevocationResponse:
    out: BatchStartViewerSessionRevocationResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors

        out["errors"] = (
            aws_sdk_ivs.types.batch_start_viewer_session_revocation_errors.deserialize_json(
                data["errors"]
            )
        )
    return out
