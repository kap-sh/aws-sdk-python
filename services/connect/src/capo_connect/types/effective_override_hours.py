"""Generated from Smithy shape ``com.amazonaws.connect#EffectiveOverrideHours``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hours_of_operation_override_year_month_day_date_format
    import capo_connect.types.override_hours


class EffectiveOverrideHours(TypedDict, closed=True):
    date: NotRequired[
        "capo_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date that the hours of operation override applies to.</p>"""
    override_hours: NotRequired["capo_connect.types.override_hours.OverrideHours"]
    """<p>Information about the hours of operation overrides that apply to a specific date.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveOverrideHours) -> dict:
    out: dict = {}
    if "date" in value:
        out["Date"] = value["date"]
    if "override_hours" in value:
        import capo_connect.types.override_hours

        out["OverrideHours"] = capo_connect.types.override_hours.serialize_json(
            value["override_hours"]
        )
    return out


def deserialize_json(data: dict) -> EffectiveOverrideHours:
    out: EffectiveOverrideHours = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        out["date"] = data["Date"]
    if "OverrideHours" in data:
        import capo_connect.types.override_hours

        out["override_hours"] = capo_connect.types.override_hours.deserialize_json(
            data["OverrideHours"]
        )
    return out
