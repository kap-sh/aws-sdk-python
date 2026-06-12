"""Generated from Smithy shape ``com.amazonaws.ram#TagFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ram.types.tag_key
    import aws_sdk_ram.types.tag_value_list


class TagFilter(TypedDict):
    tag_key: NotRequired["aws_sdk_ram.types.tag_key.TagKey"]
    """<p>The tag key. This must have a valid string value and can't be empty.</p>"""
    tag_values: NotRequired["aws_sdk_ram.types.tag_value_list.TagValueList"]
    """<p>A list of zero or more tag values. If no values are provided, then the filter matches any tag with the specified key, regardless of its value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["tagKey"] = value["tag_key"]
    if "tag_values" in value:
        import aws_sdk_ram.types.tag_value_list

        out["tagValues"] = aws_sdk_ram.types.tag_value_list.serialize_json(
            value["tag_values"]
        )
    return out


def deserialize_json(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "tagKey" in data:
        out["tag_key"] = data["tagKey"]
    if "tagValues" in data:
        import aws_sdk_ram.types.tag_value_list

        out["tag_values"] = aws_sdk_ram.types.tag_value_list.deserialize_json(
            data["tagValues"]
        )
    return out
