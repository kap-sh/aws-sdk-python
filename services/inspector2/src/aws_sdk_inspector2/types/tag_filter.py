"""Generated from Smithy shape ``com.amazonaws.inspector2#TagFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.non_empty_string
    import aws_sdk_inspector2.types.tag_comparison


class TagFilter(TypedDict, closed=True):
    comparison: "aws_sdk_inspector2.types.tag_comparison.TagComparison"
    """<p>The tag filter comparison value.</p>"""
    key: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag filter key.</p>"""
    value: "aws_sdk_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The tag filter value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector2.types.tag_comparison

    out["comparison"] = aws_sdk_inspector2.types.tag_comparison.serialize_json(
        value["comparison"]
    )
    out["key"] = value["key"]
    out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> TagFilter:
    out: TagFilter = {}  # type: ignore[typeddict-item]
    if "comparison" in data:
        import aws_sdk_inspector2.types.tag_comparison

        out["comparison"] = aws_sdk_inspector2.types.tag_comparison.deserialize_json(
            data["comparison"]
        )
    else:
        raise DeserializationError("TagFilter.comparison required")
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("TagFilter.key required")
    if "value" in data:
        out["value"] = data["value"]
    else:
        raise DeserializationError("TagFilter.value required")
    return out
