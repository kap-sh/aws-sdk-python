"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#FragmentNumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_kinesis_video_archived_media.types.fragment_number_string

FragmentNumberList: TypeAlias = list[
    "aws_sdk_kinesis_video_archived_media.types.fragment_number_string.FragmentNumberString"
]


# --- restJson1 ser/de ---
def serialize_json(value: FragmentNumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> FragmentNumberList:
    return list(data)
