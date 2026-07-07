"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#RecurrenceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.daily_settings
    import aws_sdk_ssm_contacts.types.monthly_settings
    import aws_sdk_ssm_contacts.types.number_of_on_calls
    import aws_sdk_ssm_contacts.types.recurrence_multiplier
    import aws_sdk_ssm_contacts.types.shift_coverages_map
    import aws_sdk_ssm_contacts.types.weekly_settings


class RecurrenceSettings(TypedDict, closed=True):
    monthly_settings: NotRequired[
        "aws_sdk_ssm_contacts.types.monthly_settings.MonthlySettings"
    ]
    """<p>Information about on-call rotations that recur monthly.</p>"""
    weekly_settings: NotRequired[
        "aws_sdk_ssm_contacts.types.weekly_settings.WeeklySettings"
    ]
    """<p>Information about on-call rotations that recur weekly.</p>"""
    daily_settings: NotRequired[
        "aws_sdk_ssm_contacts.types.daily_settings.DailySettings"
    ]
    """<p>Information about on-call rotations that recur daily.</p>"""
    number_of_on_calls: "aws_sdk_ssm_contacts.types.number_of_on_calls.NumberOfOnCalls"
    """<p>The number of contacts, or shift team members designated to be on call concurrently during a shift. For example, in an on-call schedule that contains ten contacts, a value of <code>2</code> designates that two of them are on call at any given time.</p>"""
    shift_coverages: NotRequired[
        "aws_sdk_ssm_contacts.types.shift_coverages_map.ShiftCoveragesMap"
    ]
    """<p>Information about the days of the week that the on-call rotation coverage includes.</p>"""
    recurrence_multiplier: (
        "aws_sdk_ssm_contacts.types.recurrence_multiplier.RecurrenceMultiplier"
    )
    """<p>The number of days, weeks, or months a single rotation lasts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecurrenceSettings) -> dict:
    out: dict = {}
    if "monthly_settings" in value:
        import aws_sdk_ssm_contacts.types.monthly_settings

        out["MonthlySettings"] = (
            aws_sdk_ssm_contacts.types.monthly_settings.serialize_aws_json_1_1(
                value["monthly_settings"]
            )
        )
    if "weekly_settings" in value:
        import aws_sdk_ssm_contacts.types.weekly_settings

        out["WeeklySettings"] = (
            aws_sdk_ssm_contacts.types.weekly_settings.serialize_aws_json_1_1(
                value["weekly_settings"]
            )
        )
    if "daily_settings" in value:
        import aws_sdk_ssm_contacts.types.daily_settings

        out["DailySettings"] = (
            aws_sdk_ssm_contacts.types.daily_settings.serialize_aws_json_1_1(
                value["daily_settings"]
            )
        )
    out["NumberOfOnCalls"] = value["number_of_on_calls"]
    if "shift_coverages" in value:
        import aws_sdk_ssm_contacts.types.shift_coverages_map

        out["ShiftCoverages"] = (
            aws_sdk_ssm_contacts.types.shift_coverages_map.serialize_aws_json_1_1(
                value["shift_coverages"]
            )
        )
    out["RecurrenceMultiplier"] = value["recurrence_multiplier"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecurrenceSettings:
    out: RecurrenceSettings = {}  # type: ignore[typeddict-item]
    if "MonthlySettings" in data:
        import aws_sdk_ssm_contacts.types.monthly_settings

        out["monthly_settings"] = (
            aws_sdk_ssm_contacts.types.monthly_settings.deserialize_aws_json_1_1(
                data["MonthlySettings"]
            )
        )
    if "WeeklySettings" in data:
        import aws_sdk_ssm_contacts.types.weekly_settings

        out["weekly_settings"] = (
            aws_sdk_ssm_contacts.types.weekly_settings.deserialize_aws_json_1_1(
                data["WeeklySettings"]
            )
        )
    if "DailySettings" in data:
        import aws_sdk_ssm_contacts.types.daily_settings

        out["daily_settings"] = (
            aws_sdk_ssm_contacts.types.daily_settings.deserialize_aws_json_1_1(
                data["DailySettings"]
            )
        )
    if "NumberOfOnCalls" in data:
        out["number_of_on_calls"] = data["NumberOfOnCalls"]
    else:
        raise DeserializationError("RecurrenceSettings.number_of_on_calls required")
    if "ShiftCoverages" in data:
        import aws_sdk_ssm_contacts.types.shift_coverages_map

        out["shift_coverages"] = (
            aws_sdk_ssm_contacts.types.shift_coverages_map.deserialize_aws_json_1_1(
                data["ShiftCoverages"]
            )
        )
    if "RecurrenceMultiplier" in data:
        out["recurrence_multiplier"] = data["RecurrenceMultiplier"]
    else:
        raise DeserializationError("RecurrenceSettings.recurrence_multiplier required")
    return out
