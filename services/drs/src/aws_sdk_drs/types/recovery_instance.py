"""Generated from Smithy shape ``com.amazonaws.drs#RecoveryInstance``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_drs.types.agent_version
    import aws_sdk_drs.types.arn
    import aws_sdk_drs.types.aws_availability_zone
    import aws_sdk_drs.types.ec2_instance_id
    import aws_sdk_drs.types.ec2_instance_state
    import aws_sdk_drs.types.iso8601_datetime_string
    import aws_sdk_drs.types.job_id
    import aws_sdk_drs.types.origin_environment
    import aws_sdk_drs.types.outpost_arn
    import aws_sdk_drs.types.recovery_instance_data_replication_info
    import aws_sdk_drs.types.recovery_instance_failback
    import aws_sdk_drs.types.recovery_instance_id
    import aws_sdk_drs.types.recovery_instance_properties
    import aws_sdk_drs.types.source_server_id
    import aws_sdk_drs.types.tags_map


class RecoveryInstance(TypedDict, closed=True):
    ec2_instance_id: NotRequired["aws_sdk_drs.types.ec2_instance_id.EC2InstanceID"]
    """<p>The EC2 instance ID of the Recovery Instance.</p>"""
    ec2_instance_state: NotRequired[
        "aws_sdk_drs.types.ec2_instance_state.EC2InstanceState"
    ]
    """<p>The state of the EC2 instance for this Recovery Instance.</p>"""
    job_id: NotRequired["aws_sdk_drs.types.job_id.JobID"]
    """<p>The ID of the Job that created the Recovery Instance.</p>"""
    recovery_instance_id: NotRequired[
        "aws_sdk_drs.types.recovery_instance_id.RecoveryInstanceID"
    ]
    """<p>The ID of the Recovery Instance.</p>"""
    source_server_id: NotRequired["aws_sdk_drs.types.source_server_id.SourceServerID"]
    """<p>The Source Server ID that this Recovery Instance is associated with.</p>"""
    arn: NotRequired["aws_sdk_drs.types.arn.ARN"]
    """<p>The ARN of the Recovery Instance.</p>"""
    tags: NotRequired["aws_sdk_drs.types.tags_map.TagsMap"]
    """<p>An array of tags that are associated with the Recovery Instance.</p>"""
    failback: NotRequired[
        "aws_sdk_drs.types.recovery_instance_failback.RecoveryInstanceFailback"
    ]
    """<p>An object representing failback related information of the Recovery Instance.</p>"""
    data_replication_info: NotRequired[
        "aws_sdk_drs.types.recovery_instance_data_replication_info.RecoveryInstanceDataReplicationInfo"
    ]
    """<p>The Data Replication Info of the Recovery Instance.</p>"""
    recovery_instance_properties: NotRequired[
        "aws_sdk_drs.types.recovery_instance_properties.RecoveryInstanceProperties"
    ]
    """<p>Properties of the Recovery Instance machine.</p>"""
    point_in_time_snapshot_date_time: NotRequired[
        "aws_sdk_drs.types.iso8601_datetime_string.ISO8601DatetimeString"
    ]
    """<p>The date and time of the Point in Time (PIT) snapshot that this Recovery Instance was launched from.</p>"""
    is_drill: NotRequired["bool"]
    """<p>Whether this Recovery Instance was created for a drill or for an actual Recovery event.</p>"""
    origin_environment: NotRequired[
        "aws_sdk_drs.types.origin_environment.OriginEnvironment"
    ]
    """<p>Environment (On Premises / AWS) of the instance that the recovery instance originated from.</p>"""
    origin_availability_zone: NotRequired[
        "aws_sdk_drs.types.aws_availability_zone.AwsAvailabilityZone"
    ]
    """<p>AWS availability zone associated with the recovery instance.</p>"""
    agent_version: NotRequired["aws_sdk_drs.types.agent_version.AgentVersion"]
    """<p>The version of the DRS agent installed on the recovery instance</p>"""
    source_outpost_arn: NotRequired["aws_sdk_drs.types.outpost_arn.OutpostARN"]
    """<p>The ARN of the source Outpost</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryInstance) -> dict:
    out: dict = {}
    if "ec2_instance_id" in value:
        out["ec2InstanceID"] = value["ec2_instance_id"]
    if "ec2_instance_state" in value:
        out["ec2InstanceState"] = value["ec2_instance_state"]
    if "job_id" in value:
        out["jobID"] = value["job_id"]
    if "recovery_instance_id" in value:
        out["recoveryInstanceID"] = value["recovery_instance_id"]
    if "source_server_id" in value:
        out["sourceServerID"] = value["source_server_id"]
    if "arn" in value:
        out["arn"] = value["arn"]
    if "tags" in value:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.serialize_json(value["tags"])
    if "failback" in value:
        import aws_sdk_drs.types.recovery_instance_failback

        out["failback"] = aws_sdk_drs.types.recovery_instance_failback.serialize_json(
            value["failback"]
        )
    if "data_replication_info" in value:
        import aws_sdk_drs.types.recovery_instance_data_replication_info

        out["dataReplicationInfo"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_info.serialize_json(
                value["data_replication_info"]
            )
        )
    if "recovery_instance_properties" in value:
        import aws_sdk_drs.types.recovery_instance_properties

        out["recoveryInstanceProperties"] = (
            aws_sdk_drs.types.recovery_instance_properties.serialize_json(
                value["recovery_instance_properties"]
            )
        )
    if "point_in_time_snapshot_date_time" in value:
        out["pointInTimeSnapshotDateTime"] = value["point_in_time_snapshot_date_time"]
    if "is_drill" in value:
        out["isDrill"] = value["is_drill"]
    if "origin_environment" in value:
        out["originEnvironment"] = value["origin_environment"]
    if "origin_availability_zone" in value:
        out["originAvailabilityZone"] = value["origin_availability_zone"]
    if "agent_version" in value:
        out["agentVersion"] = value["agent_version"]
    if "source_outpost_arn" in value:
        out["sourceOutpostArn"] = value["source_outpost_arn"]
    return out


def deserialize_json(data: dict) -> RecoveryInstance:
    out: RecoveryInstance = {}  # type: ignore[typeddict-item]
    if "ec2InstanceID" in data:
        out["ec2_instance_id"] = data["ec2InstanceID"]
    if "ec2InstanceState" in data:
        out["ec2_instance_state"] = data["ec2InstanceState"]
    if "jobID" in data:
        out["job_id"] = data["jobID"]
    if "recoveryInstanceID" in data:
        out["recovery_instance_id"] = data["recoveryInstanceID"]
    if "sourceServerID" in data:
        out["source_server_id"] = data["sourceServerID"]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "tags" in data:
        import aws_sdk_drs.types.tags_map

        out["tags"] = aws_sdk_drs.types.tags_map.deserialize_json(data["tags"])
    if "failback" in data:
        import aws_sdk_drs.types.recovery_instance_failback

        out["failback"] = aws_sdk_drs.types.recovery_instance_failback.deserialize_json(
            data["failback"]
        )
    if "dataReplicationInfo" in data:
        import aws_sdk_drs.types.recovery_instance_data_replication_info

        out["data_replication_info"] = (
            aws_sdk_drs.types.recovery_instance_data_replication_info.deserialize_json(
                data["dataReplicationInfo"]
            )
        )
    if "recoveryInstanceProperties" in data:
        import aws_sdk_drs.types.recovery_instance_properties

        out["recovery_instance_properties"] = (
            aws_sdk_drs.types.recovery_instance_properties.deserialize_json(
                data["recoveryInstanceProperties"]
            )
        )
    if "pointInTimeSnapshotDateTime" in data:
        out["point_in_time_snapshot_date_time"] = data["pointInTimeSnapshotDateTime"]
    if "isDrill" in data:
        out["is_drill"] = data["isDrill"]
    if "originEnvironment" in data:
        out["origin_environment"] = data["originEnvironment"]
    if "originAvailabilityZone" in data:
        out["origin_availability_zone"] = data["originAvailabilityZone"]
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    if "sourceOutpostArn" in data:
        out["source_outpost_arn"] = data["sourceOutpostArn"]
    return out
