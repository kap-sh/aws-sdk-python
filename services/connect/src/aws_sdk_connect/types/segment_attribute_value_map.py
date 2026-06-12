"""Generated from Smithy shape ``com.amazonaws.connect#SegmentAttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.segment_attribute_name
    import aws_sdk_connect.types.segment_attribute_value

SegmentAttributeValueMap: TypeAlias = dict[
    "aws_sdk_connect.types.segment_attribute_name.SegmentAttributeName",
    "aws_sdk_connect.types.segment_attribute_value.SegmentAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SegmentAttributeValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_connect.types.segment_attribute_value

        out[key] = aws_sdk_connect.types.segment_attribute_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SegmentAttributeValueMap:
    out: SegmentAttributeValueMap = {}
    for key, value in data.items():
        import aws_sdk_connect.types.segment_attribute_value

        out[key] = aws_sdk_connect.types.segment_attribute_value.deserialize_json(value)
    return out
