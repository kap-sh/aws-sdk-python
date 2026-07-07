"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#Image``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.image_content
    import aws_sdk_kinesis_video_archived_media.types.image_error
    import aws_sdk_kinesis_video_archived_media.types.timestamp


class Image(TypedDict, closed=True):
    time_stamp: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.timestamp.Timestamp"
    ]
    """<p>An attribute of the <code>Image</code> object that is used to extract an image from the video stream. This field is used to manage gaps on images or to better understand the pagination window.</p>"""
    error: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.image_error.ImageError"
    ]
    """<p>The error message shown when the image for the provided timestamp was not extracted due to a non-tryable error. An error will be returned if: </p> <ul> <li> <p>There is no media that exists for the specified <code>Timestamp</code>.</p> </li> </ul> <ul> <li> <p>The media for the specified time does not allow an image to be extracted. In this case the media is audio only, or the incorrect media has been ingested.</p> </li> </ul>"""
    image_content: NotRequired[
        "aws_sdk_kinesis_video_archived_media.types.image_content.ImageContent"
    ]
    """<p>An attribute of the <code>Image</code> object that is Base64 encoded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Image) -> dict:
    out: dict = {}
    if "time_stamp" in value:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["TimeStamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.serialize_json(
                value["time_stamp"]
            )
        )
    if "error" in value:
        import aws_sdk_kinesis_video_archived_media.types.image_error

        out["Error"] = (
            aws_sdk_kinesis_video_archived_media.types.image_error.serialize_json(
                value["error"]
            )
        )
    if "image_content" in value:
        out["ImageContent"] = value["image_content"]
    return out


def deserialize_json(data: dict) -> Image:
    out: Image = {}  # type: ignore[typeddict-item]
    if "TimeStamp" in data:
        import aws_sdk_kinesis_video_archived_media.types.timestamp

        out["time_stamp"] = (
            aws_sdk_kinesis_video_archived_media.types.timestamp.deserialize_json(
                data["TimeStamp"]
            )
        )
    if "Error" in data:
        import aws_sdk_kinesis_video_archived_media.types.image_error

        out["error"] = (
            aws_sdk_kinesis_video_archived_media.types.image_error.deserialize_json(
                data["Error"]
            )
        )
    if "ImageContent" in data:
        out["image_content"] = data["ImageContent"]
    return out
