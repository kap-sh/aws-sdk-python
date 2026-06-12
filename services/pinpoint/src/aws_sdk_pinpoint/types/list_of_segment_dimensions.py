"""Generated from Smithy shape ``com.amazonaws.pinpoint#ListOfSegmentDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.segment_dimensions

ListOfSegmentDimensions: TypeAlias = list[
    "aws_sdk_pinpoint.types.segment_dimensions.SegmentDimensions"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListOfSegmentDimensions) -> list:
    import aws_sdk_pinpoint.types.segment_dimensions

    out: list = []
    for item in value:
        out.append(aws_sdk_pinpoint.types.segment_dimensions.serialize_json(item))
    return out


def deserialize_json(data: list) -> ListOfSegmentDimensions:
    import aws_sdk_pinpoint.types.segment_dimensions

    out: ListOfSegmentDimensions = []
    for item in data:
        out.append(aws_sdk_pinpoint.types.segment_dimensions.deserialize_json(item))
    return out
