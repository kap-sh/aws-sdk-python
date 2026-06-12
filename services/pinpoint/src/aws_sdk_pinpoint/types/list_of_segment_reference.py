"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSegmentReference``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.segment_reference

ListOfSegmentReference: TypeAlias = list[
    "aws_sdk_pinpoint.types.segment_reference.SegmentReference"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSegmentReference) -> list:
    import aws_sdk_pinpoint.types.segment_reference

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.segment_reference.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSegmentReference:
    import aws_sdk_pinpoint.types.segment_reference

    out: ListOfSegmentReference = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.segment_reference.deserialize_json(item))
    return out
