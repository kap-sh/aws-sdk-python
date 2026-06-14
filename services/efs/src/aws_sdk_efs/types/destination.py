"""Generated from Smithy shape ``com.amazonaws.efs#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.aws_account_id
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.region_name
    import aws_sdk_efs.types.replication_status
    import aws_sdk_efs.types.role_arn
    import aws_sdk_efs.types.status_message
    import aws_sdk_efs.types.timestamp


class Destination(TypedDict):
    status: "aws_sdk_efs.types.replication_status.ReplicationStatus"
    r"""<p>Describes the status of the replication configuration. For more information about replication status, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html\">Viewing replication details</a> in the <i>Amazon EFS User Guide</i>. </p>"""
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the destination Amazon EFS file system.</p>"""
    region: "aws_sdk_efs.types.region_name.RegionName"
    """<p>The Amazon Web Services Region in which the destination file system is located.</p>"""
    last_replicated_timestamp: NotRequired["aws_sdk_efs.types.timestamp.Timestamp"]
    """<p>The time when the most recent sync was successfully completed on the destination file system. Any changes to data on the source file system that occurred before this time have been successfully replicated to the destination file system. Any changes that occurred after this time might not be fully replicated.</p>"""
    owner_id: NotRequired["aws_sdk_efs.types.aws_account_id.AwsAccountId"]
    """<p>ID of the Amazon Web Services account in which the destination file system resides.</p>"""
    status_message: NotRequired["aws_sdk_efs.types.status_message.StatusMessage"]
    r"""<p>Message that provides details about the <code>PAUSED</code> or <code>ERRROR</code> state of the replication destination configuration. For more information about replication status messages, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#restoring-backup-efsmonitoring-replication-status.html\">Viewing replication details</a> in the <i>Amazon EFS User Guide</i>. </p>"""
    role_arn: NotRequired["aws_sdk_efs.types.role_arn.RoleArn"]
    """<p>Amazon Resource Name (ARN) of the IAM role in the source account that allows Amazon EFS to perform replication on its behalf. This is optional for same-account replication and required for cross-account replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    import aws_sdk_efs.types.replication_status

    out["Status"] = aws_sdk_efs.types.replication_status.serialize_json(value["status"])
    out["FileSystemId"] = value["file_system_id"]
    out["Region"] = value["region"]
    if "last_replicated_timestamp" in value:
        import aws_sdk_efs.types.timestamp

        out["LastReplicatedTimestamp"] = aws_sdk_efs.types.timestamp.serialize_json(
            value["last_replicated_timestamp"]
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_efs.types.replication_status

        out["status"] = aws_sdk_efs.types.replication_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError("Destination.status required")
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("Destination.file_system_id required")
    if "Region" in data:
        out["region"] = data["Region"]
    else:
        raise DeserializationError("Destination.region required")
    if "LastReplicatedTimestamp" in data:
        import aws_sdk_efs.types.timestamp

        out["last_replicated_timestamp"] = aws_sdk_efs.types.timestamp.deserialize_json(
            data["LastReplicatedTimestamp"]
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    return out
