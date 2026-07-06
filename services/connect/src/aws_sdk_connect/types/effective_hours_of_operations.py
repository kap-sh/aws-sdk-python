"""Generated from Smithy shape ``com.amazonaws.connect#EffectiveHoursOfOperations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format
    import aws_sdk_connect.types.operational_hours


class EffectiveHoursOfOperations(TypedDict, closed=True):
    date: NotRequired[
        "aws_sdk_connect.types.hours_of_operation_override_year_month_day_date_format.HoursOfOperationOverrideYearMonthDayDateFormat"
    ]
    """<p>The date that the hours of operation or overrides applies to.</p>"""
    operational_hours: NotRequired[
        "aws_sdk_connect.types.operational_hours.OperationalHours"
    ]
    """<p>Information about the hours of operations with the effective override applied.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EffectiveHoursOfOperations) -> dict:
    out: dict = {}
    if "date" in value:
        out["Date"] = value["date"]
    if "operational_hours" in value:
        import aws_sdk_connect.types.operational_hours

        out["OperationalHours"] = (
            aws_sdk_connect.types.operational_hours.serialize_json(
                value["operational_hours"]
            )
        )
    return out


def deserialize_json(data: dict) -> EffectiveHoursOfOperations:
    out: EffectiveHoursOfOperations = {}  # type: ignore[typeddict-item]
    if "Date" in data:
        out["date"] = data["Date"]
    if "OperationalHours" in data:
        import aws_sdk_connect.types.operational_hours

        out["operational_hours"] = (
            aws_sdk_connect.types.operational_hours.deserialize_json(
                data["OperationalHours"]
            )
        )
    return out
