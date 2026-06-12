"""Generated from Smithy shape ``com.amazonaws.customerprofiles#SourceSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.source_segment

SourceSegmentList: TypeAlias = list[
    "aws_sdk_customer_profiles.types.source_segment.SourceSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceSegmentList) -> list:
    import aws_sdk_customer_profiles.types.source_segment

    out: list = []
    for item in value:
        out.append(aws_sdk_customer_profiles.types.source_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> SourceSegmentList:
    import aws_sdk_customer_profiles.types.source_segment

    out: SourceSegmentList = []
    for item in data:
        out.append(
            aws_sdk_customer_profiles.types.source_segment.deserialize_json(item)
        )
    return out
