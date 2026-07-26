"""Generated from Smithy shape ``com.amazonaws.connect#StringCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string
    import capo_connect.types.string_comparison_type


class StringCondition(TypedDict, closed=True):
    field_name: NotRequired["capo_connect.types.string.String"]
    """<p>The name of the field in the string condition.</p>"""
    value: NotRequired["capo_connect.types.string.String"]
    """<p>The value of the string.</p>"""
    comparison_type: NotRequired[
        "capo_connect.types.string_comparison_type.StringComparisonType"
    ]
    """<p>The type of comparison to be made when evaluating the string condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StringCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "comparison_type" in value:
        import capo_connect.types.string_comparison_type

        out["ComparisonType"] = (
            capo_connect.types.string_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> StringCondition:
    out: StringCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "ComparisonType" in data:
        import capo_connect.types.string_comparison_type

        out["comparison_type"] = (
            capo_connect.types.string_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
