"""Generated from Smithy shape ``com.amazonaws.connect#DateTimeCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.date_time_comparison_type
    import capo_connect.types.date_time_format
    import capo_connect.types.string


class DateTimeCondition(TypedDict, closed=True):
    field_name: NotRequired["capo_connect.types.string.String"]
    """<p>A name of the datetime property to be searched</p>"""
    min_value: NotRequired["capo_connect.types.date_time_format.DateTimeFormat"]
    """<p>A minimum value of the property.</p>"""
    max_value: NotRequired["capo_connect.types.date_time_format.DateTimeFormat"]
    """<p>A maximum value of the property.</p>"""
    comparison_type: NotRequired[
        "capo_connect.types.date_time_comparison_type.DateTimeComparisonType"
    ]
    """<p>Datetime property comparison type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateTimeCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "min_value" in value:
        out["MinValue"] = value["min_value"]
    if "max_value" in value:
        out["MaxValue"] = value["max_value"]
    if "comparison_type" in value:
        import capo_connect.types.date_time_comparison_type

        out["ComparisonType"] = (
            capo_connect.types.date_time_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateTimeCondition:
    out: DateTimeCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "MinValue" in data:
        out["min_value"] = data["MinValue"]
    if "MaxValue" in data:
        out["max_value"] = data["MaxValue"]
    if "ComparisonType" in data:
        import capo_connect.types.date_time_comparison_type

        out["comparison_type"] = (
            capo_connect.types.date_time_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
