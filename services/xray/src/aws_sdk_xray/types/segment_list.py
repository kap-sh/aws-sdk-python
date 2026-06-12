"""Generated from Smithy shape ``com.amazonaws.xray#SegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_xray.types.segment

SegmentList: TypeAlias = list["aws_sdk_xray.types.segment.Segment"]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentList) -> list:
    import aws_sdk_xray.types.segment

    out: list = []
    for item in value:
        out.append(aws_sdk_xray.types.segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> SegmentList:
    import aws_sdk_xray.types.segment

    out: SegmentList = []
    for item in data:
        out.append(aws_sdk_xray.types.segment.deserialize_json(item))
    return out
