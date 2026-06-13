"""Generated from Smithy shape ``com.amazonaws.qbusiness#TextSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.text_segment

TextSegmentList: TypeAlias = list["aws_sdk_qbusiness.types.text_segment.TextSegment"]


# --- restJson1 ser/de ---
def serialize_json(value: TextSegmentList) -> list:
    import aws_sdk_qbusiness.types.text_segment

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.text_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> TextSegmentList:
    import aws_sdk_qbusiness.types.text_segment

    out: TextSegmentList = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.text_segment.deserialize_json(item))
    return out
