"""Generated from Smithy shape ``com.amazonaws.ram#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ram.types.tag_key
    import capo_ram.types.tag_value_list


class TagFilter(TypedDict, closed=True):
    tag_key: NotRequired["capo_ram.types.tag_key.TagKey"]
    """<p>The tag key. This must have a valid string value and can't be empty.</p>"""
    tag_values: NotRequired["capo_ram.types.tag_value_list.TagValueList"]
    """<p>A list of zero or more tag values. If no values are provided, then the filter matches any tag with the specified key, regardless of its value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["tagKey"] = value["tag_key"]
    if "tag_values" in value:
        import capo_ram.types.tag_value_list

        out["tagValues"] = capo_ram.types.tag_value_list.serialize_json(
            value["tag_values"]
        )
    return out


def deserialize_json(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "tagKey" in data:
        out["tag_key"] = data["tagKey"]
    if "tagValues" in data:
        import capo_ram.types.tag_value_list

        out["tag_values"] = capo_ram.types.tag_value_list.deserialize_json(
            data["tagValues"]
        )
    return out
