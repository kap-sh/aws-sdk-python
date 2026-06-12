"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AttendeeIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.guid_string

AttendeeIdList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.guid_string.GuidString"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttendeeIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AttendeeIdList:
    return list(data)
