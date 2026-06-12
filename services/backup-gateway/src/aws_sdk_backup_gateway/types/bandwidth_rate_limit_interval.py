"""Generated from Smithy shape ``com.amazonaws.backupgateway#BandwidthRateLimitInterval``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_backup_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.average_upload_rate_limit
    import aws_sdk_backup_gateway.types.days_of_week
    import aws_sdk_backup_gateway.types.hour_of_day
    import aws_sdk_backup_gateway.types.minute_of_hour


class BandwidthRateLimitInterval(TypedDict):
    average_upload_rate_limit_in_bits_per_sec: NotRequired[
        "aws_sdk_backup_gateway.types.average_upload_rate_limit.AverageUploadRateLimit"
    ]
    """<p>The average upload rate limit component of the bandwidth rate limit interval, in bits per second. This field does not appear in the response if the upload rate limit is not set.</p>"""
    start_hour_of_day: "aws_sdk_backup_gateway.types.hour_of_day.HourOfDay"
    """<p>The hour of the day to start the bandwidth rate limit interval.</p>"""
    end_hour_of_day: "aws_sdk_backup_gateway.types.hour_of_day.HourOfDay"
    """<p>The hour of the day to end the bandwidth rate limit interval.</p>"""
    start_minute_of_hour: "aws_sdk_backup_gateway.types.minute_of_hour.MinuteOfHour"
    """<p>The minute of the hour to start the bandwidth rate limit interval. The interval begins at the start of that minute. To begin an interval exactly at the start of the hour, use the value <code>0</code>.</p>"""
    end_minute_of_hour: "aws_sdk_backup_gateway.types.minute_of_hour.MinuteOfHour"
    """<p>The minute of the hour to end the bandwidth rate limit interval.</p> <important> <p>The bandwidth rate limit interval ends at the end of the minute. To end an interval at the end of an hour, use the value <code>59</code>.</p> </important>"""
    days_of_week: "aws_sdk_backup_gateway.types.days_of_week.DaysOfWeek"
    """<p>The days of the week component of the bandwidth rate limit interval, represented as ordinal numbers from 0 to 6, where 0 represents Sunday and 6 represents Saturday.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthRateLimitInterval) -> dict:
    out: dict = {}
    if "average_upload_rate_limit_in_bits_per_sec" in value:
        out["AverageUploadRateLimitInBitsPerSec"] = value[
            "average_upload_rate_limit_in_bits_per_sec"
        ]
    out["StartHourOfDay"] = value["start_hour_of_day"]
    out["EndHourOfDay"] = value["end_hour_of_day"]
    out["StartMinuteOfHour"] = value["start_minute_of_hour"]
    out["EndMinuteOfHour"] = value["end_minute_of_hour"]
    import aws_sdk_backup_gateway.types.days_of_week

    out["DaysOfWeek"] = (
        aws_sdk_backup_gateway.types.days_of_week.serialize_aws_json_1_0(
            value["days_of_week"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BandwidthRateLimitInterval:
    out: BandwidthRateLimitInterval = {}  # type: ignore[typeddict-item]
    if "AverageUploadRateLimitInBitsPerSec" in data:
        out["average_upload_rate_limit_in_bits_per_sec"] = data[
            "AverageUploadRateLimitInBitsPerSec"
        ]
    if "StartHourOfDay" in data:
        out["start_hour_of_day"] = data["StartHourOfDay"]
    else:
        raise DeserializationError(
            "BandwidthRateLimitInterval.start_hour_of_day required"
        )
    if "EndHourOfDay" in data:
        out["end_hour_of_day"] = data["EndHourOfDay"]
    else:
        raise DeserializationError(
            "BandwidthRateLimitInterval.end_hour_of_day required"
        )
    if "StartMinuteOfHour" in data:
        out["start_minute_of_hour"] = data["StartMinuteOfHour"]
    else:
        raise DeserializationError(
            "BandwidthRateLimitInterval.start_minute_of_hour required"
        )
    if "EndMinuteOfHour" in data:
        out["end_minute_of_hour"] = data["EndMinuteOfHour"]
    else:
        raise DeserializationError(
            "BandwidthRateLimitInterval.end_minute_of_hour required"
        )
    if "DaysOfWeek" in data:
        import aws_sdk_backup_gateway.types.days_of_week

        out["days_of_week"] = (
            aws_sdk_backup_gateway.types.days_of_week.deserialize_aws_json_1_0(
                data["DaysOfWeek"]
            )
        )
    else:
        raise DeserializationError("BandwidthRateLimitInterval.days_of_week required")
    return out
