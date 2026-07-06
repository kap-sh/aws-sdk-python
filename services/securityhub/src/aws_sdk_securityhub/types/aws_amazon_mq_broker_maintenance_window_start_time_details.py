"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails(TypedDict, closed=True):
    day_of_week: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The day of the week on which the maintenance window falls. </p>"""
    time_of_day: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The time, in 24-hour format, on which the maintenance window falls. </p>"""
    time_zone: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p> The time zone in either the Country/City format or the UTC offset format. UTC is the default format. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails) -> dict:
    out: dict = {}
    if "day_of_week" in value:
        out["DayOfWeek"] = value["day_of_week"]
    if "time_of_day" in value:
        out["TimeOfDay"] = value["time_of_day"]
    if "time_zone" in value:
        out["TimeZone"] = value["time_zone"]
    return out


def deserialize_json(data: dict) -> AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails:
    out: AwsAmazonMqBrokerMaintenanceWindowStartTimeDetails = {}  # type: ignore[typeddict-item]
    if "DayOfWeek" in data:
        out["day_of_week"] = data["DayOfWeek"]
    if "TimeOfDay" in data:
        out["time_of_day"] = data["TimeOfDay"]
    if "TimeZone" in data:
        out["time_zone"] = data["TimeZone"]
    return out
