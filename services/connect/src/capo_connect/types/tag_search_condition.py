"""Generated from Smithy shape ``com.amazonaws.connect#TagSearchCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string_comparison_type
    import capo_connect.types.tag_key_string
    import capo_connect.types.tag_value_string


class TagSearchCondition(TypedDict, closed=True):
    tag_key: NotRequired["capo_connect.types.tag_key_string.TagKeyString"]
    """<p>The tag key used in the tag search condition.</p>"""
    tag_value: NotRequired["capo_connect.types.tag_value_string.TagValueString"]
    """<p>The tag value used in the tag search condition.</p>"""
    tag_key_comparison_type: NotRequired[
        "capo_connect.types.string_comparison_type.StringComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the tag key in tag search condition.</p>"""
    tag_value_comparison_type: NotRequired[
        "capo_connect.types.string_comparison_type.StringComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the tag value in tag search condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagSearchCondition) -> dict:
    out: dict = {}
    if "tag_key" in value:
        out["tagKey"] = value["tag_key"]
    if "tag_value" in value:
        out["tagValue"] = value["tag_value"]
    if "tag_key_comparison_type" in value:
        import capo_connect.types.string_comparison_type

        out["tagKeyComparisonType"] = (
            capo_connect.types.string_comparison_type.serialize_json(
                value["tag_key_comparison_type"]
            )
        )
    if "tag_value_comparison_type" in value:
        import capo_connect.types.string_comparison_type

        out["tagValueComparisonType"] = (
            capo_connect.types.string_comparison_type.serialize_json(
                value["tag_value_comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TagSearchCondition:
    out: TagSearchCondition = {}  # type: ignore[typeddict-item]
    if "tagKey" in data:
        out["tag_key"] = data["tagKey"]
    if "tagValue" in data:
        out["tag_value"] = data["tagValue"]
    if "tagKeyComparisonType" in data:
        import capo_connect.types.string_comparison_type

        out["tag_key_comparison_type"] = (
            capo_connect.types.string_comparison_type.deserialize_json(
                data["tagKeyComparisonType"]
            )
        )
    if "tagValueComparisonType" in data:
        import capo_connect.types.string_comparison_type

        out["tag_value_comparison_type"] = (
            capo_connect.types.string_comparison_type.deserialize_json(
                data["tagValueComparisonType"]
            )
        )
    return out
