"""Generated from Smithy shape ``com.amazonaws.connect#ContactSearchSummarySegmentAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_search_summary_segment_attribute_value
    import capo_connect.types.segment_attribute_name

ContactSearchSummarySegmentAttributes: TypeAlias = dict[
    "capo_connect.types.segment_attribute_name.SegmentAttributeName",
    "capo_connect.types.contact_search_summary_segment_attribute_value.ContactSearchSummarySegmentAttributeValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ContactSearchSummarySegmentAttributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_connect.types.contact_search_summary_segment_attribute_value

        out[key] = (
            capo_connect.types.contact_search_summary_segment_attribute_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ContactSearchSummarySegmentAttributes:
    out: ContactSearchSummarySegmentAttributes = {}
    for key, value in data.items():
        import capo_connect.types.contact_search_summary_segment_attribute_value

        out[key] = (
            capo_connect.types.contact_search_summary_segment_attribute_value.deserialize_json(
                value
            )
        )
    return out
