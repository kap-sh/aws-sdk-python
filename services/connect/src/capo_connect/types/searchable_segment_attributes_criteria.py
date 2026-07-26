"""Generated from Smithy shape ``com.amazonaws.connect#SearchableSegmentAttributesCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.searchable_segment_attribute_key
    import capo_connect.types.searchable_segment_attribute_value_list


class SearchableSegmentAttributesCriteria(TypedDict, closed=True):
    key: "capo_connect.types.searchable_segment_attribute_key.SearchableSegmentAttributeKey"
    """<p>The key containing a searchable segment attribute.</p>"""
    values: "capo_connect.types.searchable_segment_attribute_value_list.SearchableSegmentAttributeValueList"
    """<p>The list of values to search for within a searchable segment attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchableSegmentAttributesCriteria) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_connect.types.searchable_segment_attribute_value_list

    out["Values"] = (
        capo_connect.types.searchable_segment_attribute_value_list.serialize_json(
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
        import capo_connect.types.searchable_segment_attribute_value_list

        out["values"] = (
            capo_connect.types.searchable_segment_attribute_value_list.deserialize_json(
                data["Values"]
            )
        )
    else:
        raise DeserializationError(
            "SearchableSegmentAttributesCriteria.values required"
        )
    return out
