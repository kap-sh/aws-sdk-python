"""Generated from Smithy shape ``com.amazonaws.connect#SegmentAttributeValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.segment_attribute_value

SegmentAttributeValueList: TypeAlias = list[
    "aws_sdk_connect.types.segment_attribute_value.SegmentAttributeValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: SegmentAttributeValueList) -> list:
    import aws_sdk_connect.types.segment_attribute_value

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.segment_attribute_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> SegmentAttributeValueList:
    import aws_sdk_connect.types.segment_attribute_value

    out: SegmentAttributeValueList = []
    for item in data:
        out.append(aws_sdk_connect.types.segment_attribute_value.deserialize_json(item))
    return out
