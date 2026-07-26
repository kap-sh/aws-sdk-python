"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#FragmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_kinesis_video_archived_media.types.fragment

FragmentList: TypeAlias = list[
    "capo_kinesis_video_archived_media.types.fragment.Fragment"
]


# --- restJson1 ser/de ---
def serialize_json(value: FragmentList) -> list:
    import capo_kinesis_video_archived_media.types.fragment

    out: list = []
    for item in value:
        out.append(
            capo_kinesis_video_archived_media.types.fragment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FragmentList:
    import capo_kinesis_video_archived_media.types.fragment

    out: FragmentList = []
    for item in data:
        out.append(
            capo_kinesis_video_archived_media.types.fragment.deserialize_json(item)
        )
    return out
