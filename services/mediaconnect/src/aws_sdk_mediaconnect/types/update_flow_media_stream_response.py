"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowMediaStreamResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream


class UpdateFlowMediaStreamResponse(TypedDict, closed=True):
    flow_arn: NotRequired["str"]
    """<p>The ARN of the flow that is associated with the media stream that you updated. </p>"""
    media_stream: NotRequired["aws_sdk_mediaconnect.types.media_stream.MediaStream"]
    """<p>The media stream that you updated. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowMediaStreamResponse) -> dict:
    out: dict = {}
    if "flow_arn" in value:
        out["flowArn"] = value["flow_arn"]
    if "media_stream" in value:
        import aws_sdk_mediaconnect.types.media_stream

        out["mediaStream"] = aws_sdk_mediaconnect.types.media_stream.serialize_json(
            value["media_stream"]
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowMediaStreamResponse:
    out: UpdateFlowMediaStreamResponse = {}  # type: ignore[typeddict-item]
    if "flowArn" in data:
        out["flow_arn"] = data["flowArn"]
    if "mediaStream" in data:
        import aws_sdk_mediaconnect.types.media_stream

        out["media_stream"] = aws_sdk_mediaconnect.types.media_stream.deserialize_json(
            data["mediaStream"]
        )
    return out
