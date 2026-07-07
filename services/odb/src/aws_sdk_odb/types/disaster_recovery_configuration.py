"""Generated from Smithy shape ``com.amazonaws.odb#DisasterRecoveryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.disaster_recovery_type


class DisasterRecoveryConfiguration(TypedDict, closed=True):
    disaster_recovery_type: NotRequired[
        "aws_sdk_odb.types.disaster_recovery_type.DisasterRecoveryType"
    ]
    """<p>The type of disaster recovery configured for the Autonomous Database.</p>"""
    is_replicate_automatic_backups: NotRequired["bool"]
    """<p>Indicates whether automatic backups are replicated to the disaster recovery database.</p>"""
    is_snapshot_standby: NotRequired["bool"]
    """<p>Indicates whether the standby database is a snapshot standby.</p>"""
    time_snapshot_standby_enabled_till: NotRequired["datetime.datetime"]
    """<p>The date and time until which the snapshot standby database remains enabled.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisasterRecoveryConfiguration) -> dict:
    out: dict = {}
    if "disaster_recovery_type" in value:
        import aws_sdk_odb.types.disaster_recovery_type

        out["disasterRecoveryType"] = (
            aws_sdk_odb.types.disaster_recovery_type.serialize_aws_json_1_0(
                value["disaster_recovery_type"]
            )
        )
    if "is_replicate_automatic_backups" in value:
        out["isReplicateAutomaticBackups"] = value["is_replicate_automatic_backups"]
    if "is_snapshot_standby" in value:
        out["isSnapshotStandby"] = value["is_snapshot_standby"]
    if "time_snapshot_standby_enabled_till" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeSnapshotStandbyEnabledTill"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_snapshot_standby_enabled_till"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DisasterRecoveryConfiguration:
    out: DisasterRecoveryConfiguration = {}  # type: ignore[typeddict-item]
    if "disasterRecoveryType" in data:
        import aws_sdk_odb.types.disaster_recovery_type

        out["disaster_recovery_type"] = (
            aws_sdk_odb.types.disaster_recovery_type.deserialize_aws_json_1_0(
                data["disasterRecoveryType"]
            )
        )
    if "isReplicateAutomaticBackups" in data:
        out["is_replicate_automatic_backups"] = data["isReplicateAutomaticBackups"]
    if "isSnapshotStandby" in data:
        out["is_snapshot_standby"] = data["isSnapshotStandby"]
    if "timeSnapshotStandbyEnabledTill" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_snapshot_standby_enabled_till"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeSnapshotStandbyEnabledTill"]
            )
        )
    return out
