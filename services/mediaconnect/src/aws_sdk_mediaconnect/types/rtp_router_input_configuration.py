"""Generated from Smithy shape ``com.amazonaws.mediaconnect#RtpRouterInputConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediaconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.forward_error_correction_state


class RtpRouterInputConfiguration(TypedDict):
    port: "int"
    """<p>The port number used for the RTP protocol in the router input configuration.</p>"""
    forward_error_correction: NotRequired[
        "aws_sdk_mediaconnect.types.forward_error_correction_state.ForwardErrorCorrectionState"
    ]
    """<p>The state of forward error correction for the RTP protocol in the router input configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RtpRouterInputConfiguration) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    if "forward_error_correction" in value:
        import aws_sdk_mediaconnect.types.forward_error_correction_state

        out["forwardErrorCorrection"] = (
            aws_sdk_mediaconnect.types.forward_error_correction_state.serialize_json(
                value["forward_error_correction"]
            )
        )
    return out


def deserialize_json(data: dict) -> RtpRouterInputConfiguration:
    out: RtpRouterInputConfiguration = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("RtpRouterInputConfiguration.port required")
    if "forwardErrorCorrection" in data:
        import aws_sdk_mediaconnect.types.forward_error_correction_state

        out["forward_error_correction"] = (
            aws_sdk_mediaconnect.types.forward_error_correction_state.deserialize_json(
                data["forwardErrorCorrection"]
            )
        )
    return out
