"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfOutputDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.output_detail

__listOfOutputDetail: TypeAlias = list[
    "aws_sdk_mediaconvert.types.output_detail.OutputDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfOutputDetail) -> list:
    import aws_sdk_mediaconvert.types.output_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.output_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfOutputDetail:
    import aws_sdk_mediaconvert.types.output_detail

    out: __listOfOutputDetail = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.output_detail.deserialize_json(item))
    return out
