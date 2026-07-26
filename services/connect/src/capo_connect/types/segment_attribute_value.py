"""Generated from Smithy shape ``com.amazonaws.connect#SegmentAttributeValue``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.segment_attribute_value_integer
    import capo_connect.types.segment_attribute_value_list
    import capo_connect.types.segment_attribute_value_map
    import capo_connect.types.segment_attribute_value_string


class SegmentAttributeValue(TypedDict, closed=True):
    value_string: NotRequired[
        "capo_connect.types.segment_attribute_value_string.SegmentAttributeValueString"
    ]
    """<p>The value of a segment attribute.</p>"""
    value_map: NotRequired[
        "capo_connect.types.segment_attribute_value_map.SegmentAttributeValueMap"
    ]
    """<p>The value of a segment attribute.</p>"""
    value_integer: NotRequired[
        "capo_connect.types.segment_attribute_value_integer.SegmentAttributeValueInteger"
    ]
    """<p>The value of a segment attribute.</p>"""
    value_list: NotRequired[
        "capo_connect.types.segment_attribute_value_list.SegmentAttributeValueList"
    ]
    """<p>The value of a segment attribute. This is only supported for system-defined attributes, not for user-defined attributes.</p>"""
    value_arn: NotRequired[
        "capo_connect.types.segment_attribute_value_string.SegmentAttributeValueString"
    ]
    """<p>The value of a segment attribute that has to be a valid ARN. This is only supported for system-defined attributes, not for user-defined attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SegmentAttributeValue) -> dict:
    out: dict = {}
    if "value_string" in value:
        out["ValueString"] = value["value_string"]
    if "value_map" in value:
        import capo_connect.types.segment_attribute_value_map

        out["ValueMap"] = capo_connect.types.segment_attribute_value_map.serialize_json(
            value["value_map"]
        )
    if "value_integer" in value:
        out["ValueInteger"] = value["value_integer"]
    if "value_list" in value:
        import capo_connect.types.segment_attribute_value_list

        out["ValueList"] = (
            capo_connect.types.segment_attribute_value_list.serialize_json(
                value["value_list"]
            )
        )
    if "value_arn" in value:
        out["ValueArn"] = value["value_arn"]
    return out


def deserialize_json(data: dict) -> SegmentAttributeValue:
    out: SegmentAttributeValue = {}  # type: ignore[typeddict-item]
    if "ValueString" in data:
        out["value_string"] = data["ValueString"]
    if "ValueMap" in data:
        import capo_connect.types.segment_attribute_value_map

        out["value_map"] = (
            capo_connect.types.segment_attribute_value_map.deserialize_json(
                data["ValueMap"]
            )
        )
    if "ValueInteger" in data:
        out["value_integer"] = data["ValueInteger"]
    if "ValueList" in data:
        import capo_connect.types.segment_attribute_value_list

        out["value_list"] = (
            capo_connect.types.segment_attribute_value_list.deserialize_json(
                data["ValueList"]
            )
        )
    if "ValueArn" in data:
        out["value_arn"] = data["ValueArn"]
    return out
