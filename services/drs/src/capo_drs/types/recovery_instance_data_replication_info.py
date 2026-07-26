"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstanceDataReplicationInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_drs.types.aws_availability_zone
    import capo_drs.types.iso8601_datetime_string
    import capo_drs.types.outpost_arn
    import capo_drs.types.recovery_instance_data_replication_error
    import capo_drs.types.recovery_instance_data_replication_info_replicated_disks
    import capo_drs.types.recovery_instance_data_replication_initiation
    import capo_drs.types.recovery_instance_data_replication_state


class RecoveryInstanceDataReplicationInfo(TypedDict, closed=True):
    lag_duration: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>Data replication lag duration.</p>"""
    eta_date_time: NotRequired[
        "capo_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>An estimate of when the data replication will be completed.</p>"""
    replicated_disks: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_info_replicated_disks.RecoveryInstanceDataReplicationInfoReplicatedDisks"
    ]
    """<p>The disks that should be replicated.</p>"""
    data_replication_state: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_state.RecoveryInstanceDataReplicationState"
    ]
    """<p>The state of the data replication.</p>"""
    data_replication_initiation: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_initiation.RecoveryInstanceDataReplicationInitiation"
    ]
    """<p>Information about whether the data replication has been initiated.</p>"""
    data_replication_error: NotRequired[
        "capo_drs.types.recovery_instance_data_replication_error.RecoveryInstanceDataReplicationError"
    ]
    """<p>Information about Data Replication</p>"""
    staging_availability_zone: NotRequired[
        "capo_drs.types.aws_availability_zone.AwsAvailabilityZone"
    ]
    """<p>AWS Availability zone into which data is being replicated.</p>"""
    staging_outpost_arn: NotRequired["capo_drs.types.outpost_arn.OutpostARN"]
    """<p>The ARN of the staging Outpost</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstanceDataReplicationInfo) -> dict:
    out: dict = {}
    if "lag_duration" in value:
        out["lagDuration"] = value["lag_duration"]
    if "eta_date_time" in value:
        out["etaDateTime"] = value["eta_date_time"]
    if "replicated_disks" in value:
        import capo_drs.types.recovery_instance_data_replication_info_replicated_disks

        out["replicatedDisks"] = (
            capo_drs.types.recovery_instance_data_replication_info_replicated_disks.serialize_json(
                value["replicated_disks"]
            )
        )
    if "data_replication_state" in value:
        out["dataReplicationState"] = value["data_replication_state"]
    if "data_replication_initiation" in value:
        import capo_drs.types.recovery_instance_data_replication_initiation

        out["dataReplicationInitiation"] = (
            capo_drs.types.recovery_instance_data_replication_initiation.serialize_json(
                value["data_replication_initiation"]
            )
        )
    if "data_replication_error" in value:
        import capo_drs.types.recovery_instance_data_replication_error

        out["dataReplicationError"] = (
            capo_drs.types.recovery_instance_data_replication_error.serialize_json(
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
        import capo_drs.types.recovery_instance_data_replication_info_replicated_disks

        out["replicated_disks"] = (
            capo_drs.types.recovery_instance_data_replication_info_replicated_disks.deserialize_json(
                data["replicatedDisks"]
            )
        )
    if "dataReplicationState" in data:
        out["data_replication_state"] = data["dataReplicationState"]
    if "dataReplicationInitiation" in data:
        import capo_drs.types.recovery_instance_data_replication_initiation

        out["data_replication_initiation"] = (
            capo_drs.types.recovery_instance_data_replication_initiation.deserialize_json(
                data["dataReplicationInitiation"]
            )
        )
    if "dataReplicationError" in data:
        import capo_drs.types.recovery_instance_data_replication_error

        out["data_replication_error"] = (
            capo_drs.types.recovery_instance_data_replication_error.deserialize_json(
                data["dataReplicationError"]
            )
        )
    if "stagingAvailabilityZone" in data:
        out["staging_availability_zone"] = data["stagingAvailabilityZone"]
    if "stagingOutpostArn" in data:
        out["staging_outpost_arn"] = data["stagingOutpostArn"]
    return out
