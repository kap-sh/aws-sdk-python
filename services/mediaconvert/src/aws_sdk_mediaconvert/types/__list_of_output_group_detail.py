"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfOutputGroupDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.output_group_detail

__listOfOutputGroupDetail: TypeAlias = list[
    "aws_sdk_mediaconvert.types.output_group_detail.OutputGroupDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputGroupDetail) -> list:
    import aws_sdk_mediaconvert.types.output_group_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.output_group_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputGroupDetail:
    import aws_sdk_mediaconvert.types.output_group_detail

    out: __listOfOutputGroupDetail = []
    for item in data:
        out.append(
            aws_sdk_mediaconvert.types.output_group_detail.deserialize_json(item)
        )
    return out
