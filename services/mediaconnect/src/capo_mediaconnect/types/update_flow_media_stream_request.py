"""Generated from Smithy shape ``com.amazonaws.mediaconnect#UpdateFlowMediaStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.flow_arn
    import capo_mediaconnect.types.media_stream_attributes_request
    import capo_mediaconnect.types.media_stream_type


class UpdateFlowMediaStreamRequest(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_mediaconnect.types.media_stream_attributes_request.MediaStreamAttributesRequest"
    ]
    """<p> The attributes that you want to assign to the media stream.</p>"""
    clock_rate: NotRequired["int"]
    """<p>The sample rate for the stream. This value in measured in kHz. </p>"""
    description: NotRequired["str"]
    """<p>A description that can help you quickly identify what your media stream is used for. </p>"""
    flow_arn: "capo_mediaconnect.types.flow_arn.FlowArn"
    """<p> The Amazon Resource Name (ARN) of the flow that is associated with the media stream that you updated.</p>"""
    media_stream_name: "str"
    """<p> The media stream that you updated.</p>"""
    media_stream_type: NotRequired[
        "capo_mediaconnect.types.media_stream_type.MediaStreamType"
    ]
    """<p>The type of media stream. </p>"""
    video_format: NotRequired["str"]
    """<p>The resolution of the video. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowMediaStreamRequest) -> dict:
    out: dict = {}
    if "attributes" in value:
        import capo_mediaconnect.types.media_stream_attributes_request

        out["attributes"] = (
            capo_mediaconnect.types.media_stream_attributes_request.serialize_json(
                value["attributes"]
            )
        )
    if "clock_rate" in value:
        out["clockRate"] = value["clock_rate"]
    if "description" in value:
        out["description"] = value["description"]
    if "media_stream_type" in value:
        import capo_mediaconnect.types.media_stream_type

        out["mediaStreamType"] = (
            capo_mediaconnect.types.media_stream_type.serialize_json(
                value["media_stream_type"]
            )
        )
    if "video_format" in value:
        out["videoFormat"] = value["video_format"]
    return out


def deserialize_json(data: dict) -> UpdateFlowMediaStreamRequest:
    out: UpdateFlowMediaStreamRequest = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import capo_mediaconnect.types.media_stream_attributes_request

        out["attributes"] = (
            capo_mediaconnect.types.media_stream_attributes_request.deserialize_json(
                data["attributes"]
            )
        )
    if "clockRate" in data:
        out["clock_rate"] = data["clockRate"]
    if "description" in data:
        out["description"] = data["description"]
    if "mediaStreamType" in data:
        import capo_mediaconnect.types.media_stream_type

        out["media_stream_type"] = (
            capo_mediaconnect.types.media_stream_type.deserialize_json(
                data["mediaStreamType"]
            )
        )
    if "videoFormat" in data:
        out["video_format"] = data["videoFormat"]
    return out
