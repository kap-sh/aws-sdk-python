"""Generated from Smithy shape ``com.amazonaws.mediaconnect#AddMediaStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mediaconnect.types.__map_of_string
    import capo_mediaconnect.types.media_stream_attributes_request
    import capo_mediaconnect.types.media_stream_type


class AddMediaStreamRequest(TypedDict, closed=True):
    attributes: NotRequired[
        "capo_mediaconnect.types.media_stream_attributes_request.MediaStreamAttributesRequest"
    ]
    """<p> The attributes that you want to assign to the new media stream.</p>"""
    clock_rate: NotRequired["int"]
    """<p> The sample rate (in Hz) for the stream. If the media stream type is video or ancillary data, set this value to 90000. If the media stream type is audio, set this value to either 48000 or 96000.</p>"""
    description: NotRequired["str"]
    """<p> A description that can help you quickly identify what your media stream is used for.</p>"""
    media_stream_id: NotRequired["int"]
    """<p> A unique identifier for the media stream. </p>"""
    media_stream_name: NotRequired["str"]
    """<p> A name that helps you distinguish one media stream from another.</p>"""
    media_stream_type: NotRequired[
        "capo_mediaconnect.types.media_stream_type.MediaStreamType"
    ]
    """<p> The type of media stream.</p>"""
    video_format: NotRequired["str"]
    """<p> The resolution of the video.</p>"""
    media_stream_tags: NotRequired[
        "capo_mediaconnect.types.__map_of_string.__mapOfString"
    ]
    """<p> The key-value pairs that can be used to tag and organize the media stream. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddMediaStreamRequest) -> dict:
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
    if "media_stream_id" in value:
        out["mediaStreamId"] = value["media_stream_id"]
    if "media_stream_name" in value:
        out["mediaStreamName"] = value["media_stream_name"]
    if "media_stream_type" in value:
        import capo_mediaconnect.types.media_stream_type

        out["mediaStreamType"] = (
            capo_mediaconnect.types.media_stream_type.serialize_json(
                value["media_stream_type"]
            )
        )
    if "video_format" in value:
        out["videoFormat"] = value["video_format"]
    if "media_stream_tags" in value:
        import capo_mediaconnect.types.__map_of_string

        out["mediaStreamTags"] = capo_mediaconnect.types.__map_of_string.serialize_json(
            value["media_stream_tags"]
        )
    return out


def deserialize_json(data: dict) -> AddMediaStreamRequest:
    out: AddMediaStreamRequest = {}  # type: ignore[typeddict-item]
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
    if "mediaStreamId" in data:
        out["media_stream_id"] = data["mediaStreamId"]
    if "mediaStreamName" in data:
        out["media_stream_name"] = data["mediaStreamName"]
    if "mediaStreamType" in data:
        import capo_mediaconnect.types.media_stream_type

        out["media_stream_type"] = (
            capo_mediaconnect.types.media_stream_type.deserialize_json(
                data["mediaStreamType"]
            )
        )
    if "videoFormat" in data:
        out["video_format"] = data["videoFormat"]
    if "mediaStreamTags" in data:
        import capo_mediaconnect.types.__map_of_string

        out["media_stream_tags"] = (
            capo_mediaconnect.types.__map_of_string.deserialize_json(
                data["mediaStreamTags"]
            )
        )
    return out
