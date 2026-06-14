"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeMaintenanceStartTimeOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.day_of_month
    import aws_sdk_storage_gateway.types.day_of_week
    import aws_sdk_storage_gateway.types.gateway_arn
    import aws_sdk_storage_gateway.types.gateway_timezone
    import aws_sdk_storage_gateway.types.hour_of_day
    import aws_sdk_storage_gateway.types.minute_of_hour
    import aws_sdk_storage_gateway.types.software_update_preferences


class DescribeMaintenanceStartTimeOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    hour_of_day: NotRequired["aws_sdk_storage_gateway.types.hour_of_day.HourOfDay"]
    """<p>The hour component of the maintenance start time represented as <i>hh</i>, where <i>hh</i> is the hour (0 to 23). The hour of the day is in the time zone of the gateway.</p>"""
    minute_of_hour: NotRequired[
        "aws_sdk_storage_gateway.types.minute_of_hour.MinuteOfHour"
    ]
    """<p>The minute component of the maintenance start time represented as <i>mm</i>, where <i>mm</i> is the minute (0 to 59). The minute of the hour is in the time zone of the gateway.</p>"""
    day_of_week: NotRequired["aws_sdk_storage_gateway.types.day_of_week.DayOfWeek"]
    """<p>An ordinal number between 0 and 6 that represents the day of the week, where 0 represents Sunday and 6 represents Saturday. The day of week is in the time zone of the gateway.</p>"""
    day_of_month: NotRequired["aws_sdk_storage_gateway.types.day_of_month.DayOfMonth"]
    """<p>The day of the month component of the maintenance start time represented as an ordinal number from 1 to 28, where 1 represents the first day of the month. It is not possible to set the maintenance schedule to start on days 29 through 31.</p>"""
    timezone: NotRequired[
        "aws_sdk_storage_gateway.types.gateway_timezone.GatewayTimezone"
    ]
    """<p>A value that indicates the time zone that is set for the gateway. The start time and day of week specified should be in the time zone of the gateway.</p>"""
    software_update_preferences: NotRequired[
        "aws_sdk_storage_gateway.types.software_update_preferences.SoftwareUpdatePreferences"
    ]
    """<p>A set of variables indicating the software update preferences for the gateway.</p> <p>Includes <code>AutomaticUpdatePolicy</code> parameter with the following inputs:</p> <p> <code>ALL_VERSIONS</code> - Enables regular gateway maintenance updates.</p> <p> <code>EMERGENCY_VERSIONS_ONLY</code> - Disables regular gateway maintenance updates. The gateway will still receive emergency version updates on rare occasions if necessary to remedy highly critical security or durability issues. You will be notified before an emergency version update is applied. These updates are applied during your gateway's scheduled maintenance window.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceStartTimeOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "hour_of_day" in value:
        out["HourOfDay"] = value["hour_of_day"]
    if "minute_of_hour" in value:
        out["MinuteOfHour"] = value["minute_of_hour"]
    if "day_of_week" in value:
        out["DayOfWeek"] = value["day_of_week"]
    if "day_of_month" in value:
        out["DayOfMonth"] = value["day_of_month"]
    if "timezone" in value:
        out["Timezone"] = value["timezone"]
    if "software_update_preferences" in value:
        import aws_sdk_storage_gateway.types.software_update_preferences

        out["SoftwareUpdatePreferences"] = (
            aws_sdk_storage_gateway.types.software_update_preferences.serialize_aws_json_1_1(
                value["software_update_preferences"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceStartTimeOutput:
    out: DescribeMaintenanceStartTimeOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "HourOfDay" in data:
        out["hour_of_day"] = data["HourOfDay"]
    if "MinuteOfHour" in data:
        out["minute_of_hour"] = data["MinuteOfHour"]
    if "DayOfWeek" in data:
        out["day_of_week"] = data["DayOfWeek"]
    if "DayOfMonth" in data:
        out["day_of_month"] = data["DayOfMonth"]
    if "Timezone" in data:
        out["timezone"] = data["Timezone"]
    if "SoftwareUpdatePreferences" in data:
        import aws_sdk_storage_gateway.types.software_update_preferences

        out["software_update_preferences"] = (
            aws_sdk_storage_gateway.types.software_update_preferences.deserialize_aws_json_1_1(
                data["SoftwareUpdatePreferences"]
            )
        )
    return out
