"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSegmentGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.segment_group

ListOfSegmentGroup: TypeAlias = list[
    "aws_sdk_pinpoint.types.segment_group.SegmentGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSegmentGroup) -> list:
    import aws_sdk_pinpoint.types.segment_group

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.segment_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSegmentGroup:
    import aws_sdk_pinpoint.types.segment_group

    out: ListOfSegmentGroup = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.segment_group.deserialize_json(item))
    return out
