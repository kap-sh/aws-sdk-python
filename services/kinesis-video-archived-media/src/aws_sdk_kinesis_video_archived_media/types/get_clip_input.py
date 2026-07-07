"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetClipInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector
    import aws_sdk_kinesis_video_archived_media.types.resource_arn
    import aws_sdk_kinesis_video_archived_media.types.stream_name


class GetClipInput(TypedDict, closed=True):
    stream_name: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream for which to retrieve the media clip. </p> <p>You must specify either the StreamName or the StreamARN. </p>"""
    stream_arn: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream for which to retrieve the media clip. </p> <p>You must specify either the StreamName or the StreamARN. </p>"""
    clip_fragment_selector: "aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector.ClipFragmentSelector"
    """<p>The time range of the requested clip and the source of the timestamps.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClipInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector

    out["ClipFragmentSelector"] = (
        aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector.serialize_json(
            value["clip_fragment_selector"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetClipInput:
    out: GetClipInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "ClipFragmentSelector" in data:
        import aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector

        out["clip_fragment_selector"] = (
            aws_sdk_kinesis_video_archived_media.types.clip_fragment_selector.deserialize_json(
                data["ClipFragmentSelector"]
            )
        )
    else:
        raise DeserializationError("GetClipInput.clip_fragment_selector required")
    return out
