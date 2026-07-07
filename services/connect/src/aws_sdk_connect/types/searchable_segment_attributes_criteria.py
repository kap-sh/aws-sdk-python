"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributesCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.searchable_segment_attribute_key
    import aws_sdk_connect.types.searchable_segment_attribute_value_list


class SearchableSegmentAttributesCriteria(TypedDict, closed=True):
    key: "aws_sdk_connect.types.searchable_segment_attribute_key.SearchableSegmentAttributeKey"
    """<p>The key containing a searchable segment attribute.</p>"""
    values: "aws_sdk_connect.types.searchable_segment_attribute_value_list.SearchableSegmentAttributeValueList"
    """<p>The list of values to search for within a searchable segment attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributesCriteria) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import aws_sdk_connect.types.searchable_segment_attribute_value_list

    out["Values"] = (
        aws_sdk_connect.types.searchable_segment_attribute_value_list.serialize_json(
            value["values"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchableSegmentAttributesCriteria:
    out: SearchableSegmentAttributesCriteria = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    else:
        raise DeserializationError("SearchableSegmentAttributesCriteria.key required")
    if "Values" in data:
        import aws_sdk_connect.types.searchable_segment_attribute_value_list

        out["values"] = (
            aws_sdk_connect.types.searchable_segment_attribute_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError(
            "SearchableSegmentAttributesCriteria.values required"
        )
    return out
