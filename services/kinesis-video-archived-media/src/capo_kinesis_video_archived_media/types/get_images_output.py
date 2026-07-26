"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#GetImagesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.images
    import capo_kinesis_video_archived_media.types.next_token


class GetImagesOutput(TypedDict, closed=True):
    images: NotRequired["capo_kinesis_video_archived_media.types.images.Images"]
    """<p>The list of images generated from the video stream. If there is no media available for the given timestamp, the <code>NO_MEDIA</code> error will be listed in the output. If an error occurs while the image is being generated, the <code>MEDIA_ERROR</code> will be listed in the output as the cause of the missing image. </p>"""
    next_token: NotRequired[
        "capo_kinesis_video_archived_media.types.next_token.NextToken"
    ]
    """<p>The encrypted token that was used in the request to get more images.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImagesOutput) -> dict:
    out: dict = {}
    if "images" in value:
        import capo_kinesis_video_archived_media.types.images

        out["Images"] = capo_kinesis_video_archived_media.types.images.serialize_json(
            value["images"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetImagesOutput:
    out: GetImagesOutput = {}  # type: ignore[typeddict-item]
    if "Images" in data:
        import capo_kinesis_video_archived_media.types.images

        out["images"] = capo_kinesis_video_archived_media.types.images.deserialize_json(
            data["Images"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
