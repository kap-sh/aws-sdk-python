"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#Images``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.image

Images: TypeAlias = list["aws_sdk_kinesis_video_archived_media.types.image.Image"]


# --- restJson1 ser/de ---
def serialize_json(value: Images) -> list:
    import aws_sdk_kinesis_video_archived_media.types.image

    out: list = []
    for item in value:
        out.append(
            aws_sdk_kinesis_video_archived_media.types.image.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> Images:
    import aws_sdk_kinesis_video_archived_media.types.image

    out: Images = []
    for item in data:
        out.append(
            aws_sdk_kinesis_video_archived_media.types.image.deserialize_json(item)
        )
    return out
