"""Generated from Smithy shape ``com.amazonaws.odb#CrossRegionDisasterRecoveryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.arn
    import aws_sdk_odb.types.disaster_recovery_type


class CrossRegionDisasterRecoveryConfiguration(TypedDict):
    source_autonomous_database_arn: "aws_sdk_odb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the source Autonomous Database for the cross-Region disaster recovery configuration.</p>"""
    remote_disaster_recovery_type: (
        "aws_sdk_odb.types.disaster_recovery_type.DisasterRecoveryType"
    )
    """<p>The type of remote disaster recovery to configure, either Autonomous Data Guard or backup-based.</p>"""
    is_replicate_automatic_backups: NotRequired["bool"]
    """<p>Indicates whether automatic backups are replicated to the disaster recovery database.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CrossRegionDisasterRecoveryConfiguration) -> dict:
    out: dict = {}
    out["sourceAutonomousDatabaseArn"] = value["source_autonomous_database_arn"]
    import aws_sdk_odb.types.disaster_recovery_type

    out["remoteDisasterRecoveryType"] = (
        aws_sdk_odb.types.disaster_recovery_type.serialize_aws_json_1_0(
            value["remote_disaster_recovery_type"]
        )
    )
    if "is_replicate_automatic_backups" in value:
        out["isReplicateAutomaticBackups"] = value["is_replicate_automatic_backups"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CrossRegionDisasterRecoveryConfiguration:
    out: CrossRegionDisasterRecoveryConfiguration = {}  # type: ignore[typeddict-item]
    if "sourceAutonomousDatabaseArn" in data:
        out["source_autonomous_database_arn"] = data["sourceAutonomousDatabaseArn"]
    else:
        raise DeserializationError(
            "CrossRegionDisasterRecoveryConfiguration.source_autonomous_database_arn required"
        )
    if "remoteDisasterRecoveryType" in data:
        import aws_sdk_odb.types.disaster_recovery_type

        out["remote_disaster_recovery_type"] = (
            aws_sdk_odb.types.disaster_recovery_type.deserialize_aws_json_1_0(
                data["remoteDisasterRecoveryType"]
            )
        )
    else:
        raise DeserializationError(
            "CrossRegionDisasterRecoveryConfiguration.remote_disaster_recovery_type required"
        )
    if "isReplicateAutomaticBackups" in data:
        out["is_replicate_automatic_backups"] = data["isReplicateAutomaticBackups"]
    return out
