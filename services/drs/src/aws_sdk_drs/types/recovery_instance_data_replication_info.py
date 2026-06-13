"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_drs.types.aws_availability_zone
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.outpost_arn
    import aws_sdk_drs.types.recovery_instance_data_replication_error
    import aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks
    import aws_sdk_drs.types.recovery_instance_data_replication_initiation
    import aws_sdk_drs.types.recovery_instance_data_replication_state


class RecoveryInstanceDataReplicationInfo(TypedDict):
    lag_duration: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Data replication lag duration.</p>"""
    eta_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>An estimate of when the data replication will be completed.</p>"""
    replicated_disks: NotRequired[
        "aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks.RecoveryInstanceDataReplicationInfoReplicatedDisks"
    ]
    """<p>The disks that should be replicated.</p>"""
    data_replication_state: NotRequired[
        "aws_sdk_drs.types.recovery_instance_data_replication_state.RecoveryInstanceDataReplicationState"
    ]
    """<p>The state of the data replication.</p>"""
    data_replication_initiation: NotRequired[
        "aws_sdk_drs.types.recovery_instance_data_replication_initiation.RecoveryInstanceDataReplicationInitiation"
    ]
    """<p>Information about whether the data replication has been initiated.</p>"""
    data_replication_error: NotRequired[
        "aws_sdk_drs.types.recovery_instance_data_replication_error.RecoveryInstanceDataReplicationError"
    ]
    """<p>Information about Data Replication</p>"""
    staging_availability_zone: NotRequired[
        "aws_sdk_drs.types.aws_availability_zone.AwsAvailabilityZone"
    ]
    """<p>AWS Availability zone into which data is being replicated.</p>"""
    staging_outpost_arn: NotRequired["aws_sdk_drs.types.outpost_arn.OutpostARN"]
    """<p>The ARN of the staging Outpost</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInfo) -> dict:
    out: dict = {}
    if "lag_duration" in value:
        out["lagDuration"] = value["lag_duration"]
    if "eta_date_time" in value:
        out["etaDateTime"] = value["eta_date_time"]
    if "replicated_disks" in value:
        import aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks

        out["replicatedDisks"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
    if "data_replication_state" in value:
        out["dataReplicationState"] = value["data_replication_state"]
    if "data_replication_initiation" in value:
        import aws_sdk_drs.types.recovery_instance_data_replication_initiation

        out["dataReplicationInitiation"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_initiation.serialize_json(
                value["data_replication_initiation"]
            )
        )
    if "data_replication_error" in value:
        import aws_sdk_drs.types.recovery_instance_data_replication_error

        out["dataReplicationError"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_error.serialize_json(
                value["data_replication_error"]
            )
        )
    if "staging_availability_zone" in value:
        out["stagingAvailabilityZone"] = value["staging_availability_zone"]
    if "staging_outpost_arn" in value:
        out["stagingOutpostArn"] = value["staging_outpost_arn"]
    return out


def deserialize_json(data: dict) -> RecoveryInstanceDataReplicationInfo:
    out: RecoveryInstanceDataReplicationInfo = {}  # type: ignore[typeddict-item]
    if "lagDuration" in data:
        out["lag_duration"] = data["lagDuration"]
    if "etaDateTime" in data:
        out["eta_date_time"] = data["etaDateTime"]
    if "replicatedDisks" in data:
        import aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks

        out["replicated_disks"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_info_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
    if "dataReplicationState" in data:
        out["data_replication_state"] = data["dataReplicationState"]
    if "dataReplicationInitiation" in data:
        import aws_sdk_drs.types.recovery_instance_data_replication_initiation

        out["data_replication_initiation"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_initiation.deserialize_json(
                data["dataReplicationInitiation"]
            )
        )
    if "dataReplicationError" in data:
        import aws_sdk_drs.types.recovery_instance_data_replication_error

        out["data_replication_error"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_error.deserialize_json(
                data["dataReplicationError"]
            )
        )
    if "stagingAvailabilityZone" in data:
        out["staging_availability_zone"] = data["stagingAvailabilityZone"]
    if "stagingOutpostArn" in data:
        out["staging_outpost_arn"] = data["stagingOutpostArn"]
    return out
