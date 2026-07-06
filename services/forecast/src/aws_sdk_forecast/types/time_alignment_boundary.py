"""Generated from Smithy shape ``com.amazonaws.forecast#TimeAlignmentBoundary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.day_of_month
    import aws_sdk_forecast.types.day_of_week
    import aws_sdk_forecast.types.hour
    import aws_sdk_forecast.types.month


class TimeAlignmentBoundary(TypedDict, closed=True):
    month: NotRequired["aws_sdk_forecast.types.month.Month"]
    """<p>The month to use for time alignment during aggregation. The month must be in uppercase.</p>"""
    day_of_month: NotRequired["aws_sdk_forecast.types.day_of_month.DayOfMonth"]
    """<p>The day of the month to use for time alignment during aggregation.</p>"""
    day_of_week: NotRequired["aws_sdk_forecast.types.day_of_week.DayOfWeek"]
    """<p>The day of week to use for time alignment during aggregation. The day must be in uppercase.</p>"""
    hour: NotRequired["aws_sdk_forecast.types.hour.Hour"]
    """<p>The hour of day to use for time alignment during aggregation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeAlignmentBoundary) -> dict:
    out: dict = {}
    if "month" in value:
        import aws_sdk_forecast.types.month

        out["Month"] = aws_sdk_forecast.types.month.serialize_aws_json_1_1(
            value["month"]
        )
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    if "day_of_week" in value:
        import aws_sdk_forecast.types.day_of_week

        out["DayOfWeek"] = aws_sdk_forecast.types.day_of_week.serialize_aws_json_1_1(
            value["day_of_week"]
        )
    if "hour" in value:
        out["Hour"] = value["hour"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeAlignmentBoundary:
    out: TimeAlignmentBoundary = {}  # type: ignore[typeddict-item]
    if "Month" in data:
        import aws_sdk_forecast.types.month

        out["month"] = aws_sdk_forecast.types.month.deserialize_aws_json_1_1(
            data["Month"]
        )
    if "DayOfMonth" in data:
        out["day_of_month"] = data["DayOfMonth"]
    if "DayOfWeek" in data:
        import aws_sdk_forecast.types.day_of_week

        out["day_of_week"] = (
            aws_sdk_forecast.types.day_of_week.deserialize_aws_json_1_1(
                data["DayOfWeek"]
            )
        )
    if "Hour" in data:
        out["hour"] = data["Hour"]
    return out
