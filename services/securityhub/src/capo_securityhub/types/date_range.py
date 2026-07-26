"""Generated from Smithy shape ``com.amazonaws.securityhub#DateRange``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.date_range_comparison
    import capo_securityhub.types.date_range_unit
    import capo_securityhub.types.integer


class DateRange(TypedDict, closed=True):
    value: NotRequired["capo_securityhub.types.integer.Integer"]
    """<p>A date range value for the date filter.</p>"""
    unit: NotRequired["capo_securityhub.types.date_range_unit.DateRangeUnit"]
    """<p>A date range unit for the date filter.</p>"""
    comparison: NotRequired[
        "capo_securityhub.types.date_range_comparison.DateRangeComparison"
    ]
    """<p>The condition to apply to a date range filter. If you specify <code>WITHIN</code>, Security Hub filters for dates within the specified date range. If you specify <code>OLDER_THAN</code>, Security Hub filters for dates before the specified date range. If you don't specify a value, the default is <code>WITHIN</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateRange) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "unit" in value:
        import capo_securityhub.types.date_range_unit

        out["Unit"] = capo_securityhub.types.date_range_unit.serialize_json(
            value["unit"]
        )
    if "comparison" in value:
        import capo_securityhub.types.date_range_comparison

        out["Comparison"] = capo_securityhub.types.date_range_comparison.serialize_json(
            value["comparison"]
        )
    return out


def deserialize_json(data: dict) -> DateRange:
    out: DateRange = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Unit" in data:
        import capo_securityhub.types.date_range_unit

        out["unit"] = capo_securityhub.types.date_range_unit.deserialize_json(
            data["Unit"]
        )
    if "Comparison" in data:
        import capo_securityhub.types.date_range_comparison

        out["comparison"] = (
            capo_securityhub.types.date_range_comparison.deserialize_json(
                data["Comparison"]
            )
        )
    return out
