"""Generated from Smithy shape ``com.amazonaws.mediaconnect#MediaStream``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediaconnect.types.media_stream_attributes
    import aws_sdk_mediaconnect.types.media_stream_type


class MediaStream(TypedDict):
    attributes: NotRequired[
        "aws_sdk_mediaconnect.types.media_stream_attributes.MediaStreamAttributes"
    ]
    """<p> Attributes that are related to the media stream.</p>"""
    clock_rate: NotRequired["int"]
    """<p> The sample rate for the stream. This value is measured in Hz.</p>"""
    description: NotRequired["str"]
    """<p> A description that can help you quickly identify what your media stream is used for.</p>"""
    fmt: NotRequired["int"]
    """<p> The format type number (sometimes referred to as RTP payload type) of the media stream. MediaConnect assigns this value to the media stream. For ST 2110 JPEG XS outputs, you need to provide this value to the receiver.</p>"""
    media_stream_id: NotRequired["int"]
    """<p> A unique identifier for the media stream. </p>"""
    media_stream_name: NotRequired["str"]
    """<p> A name that helps you distinguish one media stream from another. </p>"""
    media_stream_type: NotRequired[
        "aws_sdk_mediaconnect.types.media_stream_type.MediaStreamType"
    ]
    """<p> The type of media stream. </p>"""
    video_format: NotRequired["str"]
    """<p> The resolution of the video. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MediaStream) -> dict:
    out: dict = {}
    if "attributes" in value:
        import aws_sdk_mediaconnect.types.media_stream_attributes

        out["attributes"] = (
            aws_sdk_mediaconnect.types.media_stream_attributes.serialize_json(
                value["attributes"]
            )
        )
    if "clock_rate" in value:
        out["clockRate"] = value["clock_rate"]
    if "description" in value:
        out["description"] = value["description"]
    if "fmt" in value:
        out["fmt"] = value["fmt"]
    if "media_stream_id" in value:
        out["mediaStreamId"] = value["media_stream_id"]
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    if "media_stream_type" in value:
        import aws_sdk_mediaconnect.types.media_stream_type

        out["mediaStreamType"] = (
            aws_sdk_mediaconnect.types.media_stream_type.serialize_json(
                value["media_stream_type"]
            )
        )
    if "video_format" in value:
        out["videoFormat"] = value["video_format"]
    return out


def deserialize_json(data: dict) -> MediaStream:
    out: MediaStream = {}  # type: ignore[typeddict-item]
    if "attributes" in data:
        import aws_sdk_mediaconnect.types.media_stream_attributes

        out["attributes"] = (
            aws_sdk_mediaconnect.types.media_stream_attributes.deserialize_json(
                data["attributes"]
            )
        )
    if "clockRate" in data:
        out["clock_rate"] = data["clockRate"]
    if "description" in data:
        out["description"] = data["description"]
    if "fmt" in data:
        out["fmt"] = data["fmt"]
    if "mediaStreamId" in data:
        out["media_stream_id"] = data["mediaStreamId"]
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    if "mediaStreamType" in data:
        import aws_sdk_mediaconnect.types.media_stream_type

        out["media_stream_type"] = (
            aws_sdk_mediaconnect.types.media_stream_type.deserialize_json(
                data["mediaStreamType"]
            )
        )
    if "videoFormat" in data:
        out["video_format"] = data["videoFormat"]
    return out
