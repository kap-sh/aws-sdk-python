"""Generated from Smithy shape ``com.amazonaws.odb#LongTermBackupSchedule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.repeat_cadence


class LongTermBackupSchedule(TypedDict):
    is_disabled: NotRequired["bool"]
    """<p>Indicates whether the long-term backup schedule is disabled.</p>"""
    repeat_cadence: NotRequired["aws_sdk_odb.types.repeat_cadence.RepeatCadence"]
    """<p>The cadence at which long-term backups are taken.</p>"""
    retention_period_in_days: NotRequired["int"]
    """<p>The retention period, in days, for long-term backups.</p>"""
    time_of_backup: NotRequired["datetime.datetime"]
    """<p>The date and time at which the long-term backup is taken.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LongTermBackupSchedule) -> dict:
    out: dict = {}
    if "is_disabled" in value:
        out["isDisabled"] = value["is_disabled"]
    if "repeat_cadence" in value:
        import aws_sdk_odb.types.repeat_cadence

        out["repeatCadence"] = aws_sdk_odb.types.repeat_cadence.serialize_aws_json_1_0(
            value["repeat_cadence"]
        )
    if "retention_period_in_days" in value:
        out["retentionPeriodInDays"] = value["retention_period_in_days"]
    if "time_of_backup" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeOfBackup"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_of_backup"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> LongTermBackupSchedule:
    out: LongTermBackupSchedule = {}  # type: ignore[typeddict-item]
    if "isDisabled" in data:
        out["is_disabled"] = data["isDisabled"]
    if "repeatCadence" in data:
        import aws_sdk_odb.types.repeat_cadence

        out["repeat_cadence"] = (
            aws_sdk_odb.types.repeat_cadence.deserialize_aws_json_1_0(
                data["repeatCadence"]
            )
        )
    if "retentionPeriodInDays" in data:
        out["retention_period_in_days"] = data["retentionPeriodInDays"]
    if "timeOfBackup" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_of_backup"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeOfBackup"]
            )
        )
    return out
