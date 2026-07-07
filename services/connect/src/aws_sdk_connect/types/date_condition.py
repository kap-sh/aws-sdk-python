"""Generated from Smithy shape ``com.amazonaws.connect#DateCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.date_comparison_type
    import aws_sdk_connect.types.date_year_month_day_format
    import aws_sdk_connect.types.string


class DateCondition(TypedDict, closed=True):
    field_name: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>An object to specify the hours of operation override date field.</p>"""
    value: NotRequired[
        "aws_sdk_connect.types.date_year_month_day_format.DateYearMonthDayFormat"
    ]
    """<p>An object to specify the hours of operation override date value.</p>"""
    comparison_type: NotRequired[
        "aws_sdk_connect.types.date_comparison_type.DateComparisonType"
    ]
    """<p>An object to specify the hours of operation override date condition <code>comparisonType</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateCondition) -> dict:
    out: dict = {}
    if "field_name" in value:
        out["FieldName"] = value["field_name"]
    if "value" in value:
        out["Value"] = value["value"]
    if "comparison_type" in value:
        import aws_sdk_connect.types.date_comparison_type

        out["ComparisonType"] = (
            aws_sdk_connect.types.date_comparison_type.serialize_json(
                value["comparison_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateCondition:
    out: DateCondition = {}  # type: ignore[typeddict-item]
    if "FieldName" in data:
        out["field_name"] = data["FieldName"]
    if "Value" in data:
        out["value"] = data["Value"]
    if "ComparisonType" in data:
        import aws_sdk_connect.types.date_comparison_type

        out["comparison_type"] = (
            aws_sdk_connect.types.date_comparison_type.deserialize_json(
                data["ComparisonType"]
            )
        )
    return out
