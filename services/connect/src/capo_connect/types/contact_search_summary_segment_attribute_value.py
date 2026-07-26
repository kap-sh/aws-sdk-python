"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummarySegmentAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.segment_attribute_value_map
    import capo_connect.types.segment_attribute_value_string


class ContactSearchSummarySegmentAttributeValue(TypedDict, closed=True):
    value_string: NotRequired[
        "capo_connect.types.segment_attribute_value_string.SegmentAttributeValueString"
    ]
    """<p>The value of a segment attribute represented as a string.</p>"""
    value_map: NotRequired[
        "capo_connect.types.segment_attribute_value_map.SegmentAttributeValueMap"
    ]
    """<p>The key and value of a segment attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactSearchSummarySegmentAttributeValue) -> dict:
    out: dict = {}
    if "value_string" in value:
        out["ValueString"] = value["value_string"]
    if "value_map" in value:
        import capo_connect.types.segment_attribute_value_map

        out["ValueMap"] = capo_connect.types.segment_attribute_value_map.serialize_json(
            value["value_map"]
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummarySegmentAttributeValue:
    out: ContactSearchSummarySegmentAttributeValue = {}  # type: ignore[typeddict-item]
    if "ValueString" in data:
        out["value_string"] = data["ValueString"]
    if "ValueMap" in data:
        import capo_connect.types.segment_attribute_value_map

        out["value_map"] = (
            capo_connect.types.segment_attribute_value_map.deserialize_json(
                data["ValueMap"]
            )
        )
    return out
