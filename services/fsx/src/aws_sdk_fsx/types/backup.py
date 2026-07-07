"""Generated from Smithy shape ``com.amazonaws.fsx#Backup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.active_directory_backup_attributes
    import aws_sdk_fsx.types.aws_account_id
    import aws_sdk_fsx.types.backup_failure_details
    import aws_sdk_fsx.types.backup_id
    import aws_sdk_fsx.types.backup_lifecycle
    import aws_sdk_fsx.types.backup_type
    import aws_sdk_fsx.types.creation_time
    import aws_sdk_fsx.types.file_system
    import aws_sdk_fsx.types.kms_key_id
    import aws_sdk_fsx.types.progress_percent
    import aws_sdk_fsx.types.region
    import aws_sdk_fsx.types.resource_arn
    import aws_sdk_fsx.types.resource_type
    import aws_sdk_fsx.types.size_in_bytes
    import aws_sdk_fsx.types.tags
    import aws_sdk_fsx.types.volume


class Backup(TypedDict, closed=True):
    backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]
    """<p>The ID of the backup.</p>"""
    lifecycle: NotRequired["aws_sdk_fsx.types.backup_lifecycle.BackupLifecycle"]
    """<p>The lifecycle status of the backup.</p> <ul> <li> <p> <code>AVAILABLE</code> - The backup is fully available.</p> </li> <li> <p> <code>PENDING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx hasn't started creating the backup.</p> </li> <li> <p> <code>CREATING</code> - Amazon FSx is creating the backup.</p> </li> <li> <p> <code>TRANSFERRING</code> - For user-initiated backups on Lustre file systems only; Amazon FSx is transferring the backup to Amazon S3.</p> </li> <li> <p> <code>COPYING</code> - Amazon FSx is copying the backup.</p> </li> <li> <p> <code>DELETED</code> - Amazon FSx deleted the backup and it's no longer available.</p> </li> <li> <p> <code>FAILED</code> - Amazon FSx couldn't finish the backup.</p> </li> </ul>"""
    failure_details: NotRequired[
        "aws_sdk_fsx.types.backup_failure_details.BackupFailureDetails"
    ]
    """<p>Details explaining any failures that occurred when creating a backup.</p>"""
    type: NotRequired["aws_sdk_fsx.types.backup_type.BackupType"]
    """<p>The type of the file-system backup.</p>"""
    progress_percent: NotRequired["aws_sdk_fsx.types.progress_percent.ProgressPercent"]
    creation_time: NotRequired["aws_sdk_fsx.types.creation_time.CreationTime"]
    """<p>The time when a particular backup was created.</p>"""
    kms_key_id: NotRequired["aws_sdk_fsx.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt the backup of the Amazon FSx file system's data at rest. </p>"""
    resource_arn: NotRequired["aws_sdk_fsx.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) for the backup resource.</p>"""
    tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    """<p>The tags associated with a particular file system.</p>"""
    file_system: NotRequired["aws_sdk_fsx.types.file_system.FileSystem"]
    """<p>The metadata of the file system associated with the backup. This metadata is persisted even if the file system is deleted.</p>"""
    directory_information: NotRequired[
        "aws_sdk_fsx.types.active_directory_backup_attributes.ActiveDirectoryBackupAttributes"
    ]
    """<p>The configuration of the self-managed Microsoft Active Directory directory to which the Windows File Server instance is joined.</p>"""
    owner_id: NotRequired["aws_sdk_fsx.types.aws_account_id.AWSAccountId"]
    source_backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]
    source_backup_region: NotRequired["aws_sdk_fsx.types.region.Region"]
    """<p>The source Region of the backup. Specifies the Region from where this backup is copied.</p>"""
    resource_type: NotRequired["aws_sdk_fsx.types.resource_type.ResourceType"]
    """<p>Specifies the resource type that's backed up.</p>"""
    volume: NotRequired["aws_sdk_fsx.types.volume.Volume"]
    size_in_bytes: NotRequired["aws_sdk_fsx.types.size_in_bytes.SizeInBytes"]
    """<p> The size of the backup in bytes. This represents the amount of data that the file system would contain if you restore this backup. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Backup) -> dict:
    out: dict = {}
    if "backup_id" in value:
        out["BackupId"] = value["backup_id"]
    if "lifecycle" in value:
        import aws_sdk_fsx.types.backup_lifecycle

        out["Lifecycle"] = aws_sdk_fsx.types.backup_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "failure_details" in value:
        import aws_sdk_fsx.types.backup_failure_details

        out["FailureDetails"] = (
            aws_sdk_fsx.types.backup_failure_details.serialize_aws_json_1_1(
                value["failure_details"]
            )
        )
    if "type" in value:
        import aws_sdk_fsx.types.backup_type

        out["Type"] = aws_sdk_fsx.types.backup_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "progress_percent" in value:
        out["ProgressPercent"] = value["progress_percent"]
    if "creation_time" in value:
        import aws_sdk_fsx.types.creation_time

        out["CreationTime"] = aws_sdk_fsx.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "resource_arn" in value:
        out["ResourceARN"] = value["resource_arn"]
    if "tags" in value:
        import aws_sdk_fsx.types.tags

        out["Tags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(value["tags"])
    if "file_system" in value:
        import aws_sdk_fsx.types.file_system

        out["FileSystem"] = aws_sdk_fsx.types.file_system.serialize_aws_json_1_1(
            value["file_system"]
        )
    if "directory_information" in value:
        import aws_sdk_fsx.types.active_directory_backup_attributes

        out["DirectoryInformation"] = (
            aws_sdk_fsx.types.active_directory_backup_attributes.serialize_aws_json_1_1(
                value["directory_information"]
            )
        )
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "source_backup_id" in value:
        out["SourceBackupId"] = value["source_backup_id"]
    if "source_backup_region" in value:
        out["SourceBackupRegion"] = value["source_backup_region"]
    if "resource_type" in value:
        import aws_sdk_fsx.types.resource_type

        out["ResourceType"] = aws_sdk_fsx.types.resource_type.serialize_aws_json_1_1(
            value["resource_type"]
        )
    if "volume" in value:
        import aws_sdk_fsx.types.volume

        out["Volume"] = aws_sdk_fsx.types.volume.serialize_aws_json_1_1(value["volume"])
    if "size_in_bytes" in value:
        out["SizeInBytes"] = value["size_in_bytes"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Backup:
    out: Backup = {}  # type: ignore[typeddict-item]
    if "BackupId" in data:
        out["backup_id"] = data["BackupId"]
    if "Lifecycle" in data:
        import aws_sdk_fsx.types.backup_lifecycle

        out["lifecycle"] = aws_sdk_fsx.types.backup_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if "FailureDetails" in data:
        import aws_sdk_fsx.types.backup_failure_details

        out["failure_details"] = (
            aws_sdk_fsx.types.backup_failure_details.deserialize_aws_json_1_1(
                data["FailureDetails"]
            )
        )
    if "Type" in data:
        import aws_sdk_fsx.types.backup_type

        out["type"] = aws_sdk_fsx.types.backup_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "ProgressPercent" in data:
        out["progress_percent"] = data["ProgressPercent"]
    if "CreationTime" in data:
        import aws_sdk_fsx.types.creation_time

        out["creation_time"] = aws_sdk_fsx.types.creation_time.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "ResourceARN" in data:
        out["resource_arn"] = data["ResourceARN"]
    if "Tags" in data:
        import aws_sdk_fsx.types.tags

        out["tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(data["Tags"])
    if "FileSystem" in data:
        import aws_sdk_fsx.types.file_system

        out["file_system"] = aws_sdk_fsx.types.file_system.deserialize_aws_json_1_1(
            data["FileSystem"]
        )
    if "DirectoryInformation" in data:
        import aws_sdk_fsx.types.active_directory_backup_attributes

        out["directory_information"] = (
            aws_sdk_fsx.types.active_directory_backup_attributes.deserialize_aws_json_1_1(
                data["DirectoryInformation"]
            )
        )
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    if "SourceBackupId" in data:
        out["source_backup_id"] = data["SourceBackupId"]
    if "SourceBackupRegion" in data:
        out["source_backup_region"] = data["SourceBackupRegion"]
    if "ResourceType" in data:
        import aws_sdk_fsx.types.resource_type

        out["resource_type"] = aws_sdk_fsx.types.resource_type.deserialize_aws_json_1_1(
            data["ResourceType"]
        )
    if "Volume" in data:
        import aws_sdk_fsx.types.volume

        out["volume"] = aws_sdk_fsx.types.volume.deserialize_aws_json_1_1(
            data["Volume"]
        )
    if "SizeInBytes" in data:
        out["size_in_bytes"] = data["SizeInBytes"]
    return out
