"""Generated from Smithy shape ``com.amazonaws.connect#SegmentAttributeValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.segment_attribute_name
    import capo_connect.types.segment_attribute_value

SegmentAttributeValueMap: TypeAlias = dict[
    "capo_connect.types.segment_attribute_name.SegmentAttributeName",
    "capo_connect.types.segment_attribute_value.SegmentAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: SegmentAttributeValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.segment_attribute_value

        out[key] = capo_connect.types.segment_attribute_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> SegmentAttributeValueMap:
    out: SegmentAttributeValueMap = {}
    for key, value in data.items():
        import capo_connect.types.segment_attribute_value

        out[key] = capo_connect.types.segment_attribute_value.deserialize_json(value)
    return out
