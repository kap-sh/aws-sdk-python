"""Generated from Smithy shape ``com.amazonaws.groundstation#AzElSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.az_el_segment

AzElSegmentList: TypeAlias = list[
    "aws_sdk_groundstation.types.az_el_segment.AzElSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: AzElSegmentList) -> list:
    import aws_sdk_groundstation.types.az_el_segment

    out: list = []
    for item in value:
        out.append(aws_sdk_groundstation.types.az_el_segment.serialize_json(item))
    return out


def deserialize_json(data: list) -> AzElSegmentList:
    import aws_sdk_groundstation.types.az_el_segment

    out: AzElSegmentList = []
    for item in data:
        out.append(aws_sdk_groundstation.types.az_el_segment.deserialize_json(item))
    return out
