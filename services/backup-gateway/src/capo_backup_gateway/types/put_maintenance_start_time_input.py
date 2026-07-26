"""Generated from Smithy shape ``com.amazonaws.backupgateway#PutMaintenanceStartTimeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup_gateway.types.day_of_month
    import capo_backup_gateway.types.day_of_week
    import capo_backup_gateway.types.gateway_arn
    import capo_backup_gateway.types.hour_of_day
    import capo_backup_gateway.types.minute_of_hour


class PutMaintenanceStartTimeInput(TypedDict, closed=True):
    gateway_arn: "capo_backup_gateway.types.gateway_arn.GatewayArn"
    """<p>The Amazon Resource Name (ARN) for the gateway, used to specify its maintenance start time.</p>"""
    hour_of_day: "capo_backup_gateway.types.hour_of_day.HourOfDay"
    """<p>The hour of the day to start maintenance on a gateway.</p>"""
    minute_of_hour: "capo_backup_gateway.types.minute_of_hour.MinuteOfHour"
    """<p>The minute of the hour to start maintenance on a gateway.</p>"""
    day_of_week: NotRequired["capo_backup_gateway.types.day_of_week.DayOfWeek"]
    """<p>The day of the week to start maintenance on a gateway.</p>"""
    day_of_month: NotRequired["capo_backup_gateway.types.day_of_month.DayOfMonth"]
    """<p>The day of the month start maintenance on a gateway.</p> <p>Valid values range from <code>Sunday</code> to <code>Saturday</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PutMaintenanceStartTimeInput) -> dict:
    out: dict = {}
    out["GatewayArn"] = value["gateway_arn"]
    out["HourOfDay"] = value["hour_of_day"]
    out["MinuteOfHour"] = value["minute_of_hour"]
    if "day_of_week" in value:
        out["DayOfWeek"] = value["day_of_week"]
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    return out


def deserialize_aws_json_1_0(data: dict) -> PutMaintenanceStartTimeInput:
    out: PutMaintenanceStartTimeInput = {}  # type: ignore[typeddict-item]
    if "GatewayArn" in data:
        out["gateway_arn"] = data["GatewayArn"]
    else:
        raise DeserializationError("PutMaintenanceStartTimeInput.gateway_arn required")
    if "HourOfDay" in data:
        out["hour_of_day"] = data["HourOfDay"]
    else:
        raise DeserializationError("PutMaintenanceStartTimeInput.hour_of_day required")
    if "MinuteOfHour" in data:
        out["minute_of_hour"] = data["MinuteOfHour"]
    else:
        raise DeserializationError(
            "PutMaintenanceStartTimeInput.minute_of_hour required"
        )
    if "DayOfWeek" in data:
        out["day_of_week"] = data["DayOfWeek"]
    if "DayOfMonth" in data:
        out["day_of_month"] = data["DayOfMonth"]
    return out
