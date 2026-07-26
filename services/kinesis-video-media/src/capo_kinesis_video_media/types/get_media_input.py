"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#GetMediaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_video_media.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_video_media.types.resource_arn
    import capo_kinesis_video_media.types.start_selector
    import capo_kinesis_video_media.types.stream_name


class GetMediaInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis_video_media.types.stream_name.StreamName"]
    """<p>The Kinesis video stream name from where you want to get the media content. If you don't specify the <code>streamName</code>, you must specify the <code>streamARN</code>.</p>"""
    stream_arn: NotRequired["capo_kinesis_video_media.types.resource_arn.ResourceARN"]
    """<p>The ARN of the stream from where you want to get the media content. If you don't specify the <code>streamARN</code>, you must specify the <code>streamName</code>.</p>"""
    start_selector: "capo_kinesis_video_media.types.start_selector.StartSelector"
    """<p>Identifies the starting chunk to get from the specified stream. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import capo_kinesis_video_media.types.start_selector

    out["StartSelector"] = capo_kinesis_video_media.types.start_selector.serialize_json(
        value["start_selector"]
    )
    return out


def deserialize_json(data: dict) -> GetMediaInput:
    out: GetMediaInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StartSelector" in data:
        import capo_kinesis_video_media.types.start_selector

        out["start_selector"] = (
            capo_kinesis_video_media.types.start_selector.deserialize_json(
                data["StartSelector"]
            )
        )
    else:
        raise DeserializationError("GetMediaInput.start_selector required")
    return out
