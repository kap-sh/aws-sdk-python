"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetMediaForFragmentListInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video_archived_media.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.fragment_number_list
    import aws_sdk_kinesis_video_archived_media.types.resource_arn
    import aws_sdk_kinesis_video_archived_media.types.stream_name


class GetMediaForFragmentListInput(TypedDict):
    stream_name: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.stream_name.StreamName"
    ]
    """<p>The name of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamARN</code> parameter.</p>"""
    stream_arn: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.resource_arn.ResourceARN"
    ]
    """<p>The Amazon Resource Name (ARN) of the stream from which to retrieve fragment media. Specify either this parameter or the <code>StreamName</code> parameter.</p>"""
    fragments: "aws_sdk_kinesis_video_archived_media.types.fragment_number_list.FragmentNumberList"
    """<p>A list of the numbers of fragments for which to retrieve media. You retrieve these values with <a>ListFragments</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMediaForFragmentListInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    import aws_sdk_kinesis_video_archived_media.types.fragment_number_list

    out["Fragments"] = (
        aws_sdk_kinesis_video_archived_media.types.fragment_number_list.serialize_json(
            value["fragments"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetMediaForFragmentListInput:
    out: GetMediaForFragmentListInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "Fragments" in data:
        import aws_sdk_kinesis_video_archived_media.types.fragment_number_list

        out["fragments"] = (
            aws_sdk_kinesis_video_archived_media.types.fragment_number_list.deserialize_json(
                data["Fragments"]
            )
        )
    else:
        raise DeserializationError("GetMediaForFragmentListInput.fragments required")
    return out
