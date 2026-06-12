"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#HandOffTime``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.hour_of_day
    import aws_sdk_ssm_contacts.types.minute_of_hour


class HandOffTime(TypedDict):
    hour_of_day: "aws_sdk_ssm_contacts.types.hour_of_day.HourOfDay"
    """<p>The hour when an on-call rotation shift begins or ends.</p>"""
    minute_of_hour: "aws_sdk_ssm_contacts.types.minute_of_hour.MinuteOfHour"
    """<p>The minute when an on-call rotation shift begins or ends.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HandOffTime) -> dict:
    out: dict = {}
    out["HourOfDay"] = value.get("hour_of_day", 0)
    out["MinuteOfHour"] = value.get("minute_of_hour", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> HandOffTime:
    out: HandOffTime = {}  # type: ignore[typeddict-item]
    if "HourOfDay" in data:
        out["hour_of_day"] = data["HourOfDay"]
    else:
        out["hour_of_day"] = 0
    if "MinuteOfHour" in data:
        out["minute_of_hour"] = data["MinuteOfHour"]
    else:
        out["minute_of_hour"] = 0
    return out
