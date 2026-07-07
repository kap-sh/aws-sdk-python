"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_redshift_serverless.types.account_id_list
    import aws_sdk_redshift_serverless.types.kms_key_id
    import aws_sdk_redshift_serverless.types.snapshot_status


class Snapshot(TypedDict, closed=True):
    namespace_name: NotRequired["str"]
    """<p>The name of the namepsace.</p>"""
    namespace_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the namespace the snapshot was created from.</p>"""
    snapshot_name: NotRequired["str"]
    """<p>The name of the snapshot.</p>"""
    snapshot_create_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the snapshot was created.</p>"""
    admin_username: NotRequired["str"]
    """<p>The username of the database within a snapshot.</p>"""
    status: NotRequired[
        "aws_sdk_redshift_serverless.types.snapshot_status.SnapshotStatus"
    ]
    """<p>The status of the snapshot.</p>"""
    kms_key_id: NotRequired["aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"]
    """<p>The unique identifier of the KMS key used to encrypt the snapshot.</p>"""
    owner_account: NotRequired["str"]
    """<p>The owner Amazon Web Services; account of the snapshot.</p>"""
    total_backup_size_in_mega_bytes: NotRequired["float"]
    """<p>The total size, in megabytes, of how big the snapshot is.</p>"""
    actual_incremental_backup_size_in_mega_bytes: NotRequired["float"]
    """<p>The size of the incremental backup in megabytes.</p>"""
    backup_progress_in_mega_bytes: NotRequired["float"]
    """<p>The size in megabytes of the data that has been backed up to a snapshot.</p>"""
    current_backup_rate_in_mega_bytes_per_second: NotRequired["float"]
    """<p>The rate at which data is backed up into a snapshot in megabytes per second.</p>"""
    estimated_seconds_to_completion: NotRequired["int"]
    """<p>The estimated amount of seconds until the snapshot completes backup.</p>"""
    elapsed_time_in_seconds: NotRequired["int"]
    """<p>The amount of time it took to back up data into a snapshot.</p>"""
    snapshot_retention_period: NotRequired["int"]
    """<p>The period of time, in days, of how long the snapshot is retained.</p>"""
    snapshot_remaining_days: NotRequired["int"]
    """<p>The amount of days until the snapshot is deleted.</p>"""
    snapshot_retention_start_time: NotRequired["datetime.datetime"]
    """<p>The timestamp of when data within the snapshot started getting retained.</p>"""
    snapshot_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) of the snapshot.</p>"""
    accounts_with_restore_access: NotRequired[
        "aws_sdk_redshift_serverless.types.account_id_list.AccountIdList"
    ]
    """<p>All of the Amazon Web Services accounts that have access to restore a snapshot to a namespace.</p>"""
    accounts_with_provisioned_restore_access: NotRequired[
        "aws_sdk_redshift_serverless.types.account_id_list.AccountIdList"
    ]
    """<p>All of the Amazon Web Services accounts that have access to restore a snapshot to a provisioned cluster.</p>"""
    admin_password_secret_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) for the namespace's admin user credentials secret.</p>"""
    admin_password_secret_kms_key_id: NotRequired[
        "aws_sdk_redshift_serverless.types.kms_key_id.KmsKeyId"
    ]
    """<p>The ID of the Key Management Service (KMS) key used to encrypt and store the namespace's admin credentials secret.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Snapshot) -> dict:
    out: dict = {}
    if "namespace_name" in value:
        out["namespaceName"] = value["namespace_name"]
    if "namespace_arn" in value:
        out["namespaceArn"] = value["namespace_arn"]
    if "snapshot_name" in value:
        out["snapshotName"] = value["snapshot_name"]
    if "snapshot_create_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["snapshotCreateTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["snapshot_create_time"]
            )
        )
    if "admin_username" in value:
        out["adminUsername"] = value["admin_username"]
    if "status" in value:
        out["status"] = value["status"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "owner_account" in value:
        out["ownerAccount"] = value["owner_account"]
    if "total_backup_size_in_mega_bytes" in value:
        out["totalBackupSizeInMegaBytes"] = value["total_backup_size_in_mega_bytes"]
    if "actual_incremental_backup_size_in_mega_bytes" in value:
        out["actualIncrementalBackupSizeInMegaBytes"] = value[
            "actual_incremental_backup_size_in_mega_bytes"
        ]
    if "backup_progress_in_mega_bytes" in value:
        out["backupProgressInMegaBytes"] = value["backup_progress_in_mega_bytes"]
    if "current_backup_rate_in_mega_bytes_per_second" in value:
        out["currentBackupRateInMegaBytesPerSecond"] = value[
            "current_backup_rate_in_mega_bytes_per_second"
        ]
    if "estimated_seconds_to_completion" in value:
        out["estimatedSecondsToCompletion"] = value["estimated_seconds_to_completion"]
    if "elapsed_time_in_seconds" in value:
        out["elapsedTimeInSeconds"] = value["elapsed_time_in_seconds"]
    if "snapshot_retention_period" in value:
        out["snapshotRetentionPeriod"] = value["snapshot_retention_period"]
    if "snapshot_remaining_days" in value:
        out["snapshotRemainingDays"] = value["snapshot_remaining_days"]
    if "snapshot_retention_start_time" in value:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["snapshotRetentionStartTime"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.serialize_aws_json_1_1(
                value["snapshot_retention_start_time"]
            )
        )
    if "snapshot_arn" in value:
        out["snapshotArn"] = value["snapshot_arn"]
    if "accounts_with_restore_access" in value:
        import aws_sdk_redshift_serverless.types.account_id_list

        out["accountsWithRestoreAccess"] = (
            aws_sdk_redshift_serverless.types.account_id_list.serialize_aws_json_1_1(
                value["accounts_with_restore_access"]
            )
        )
    if "accounts_with_provisioned_restore_access" in value:
        import aws_sdk_redshift_serverless.types.account_id_list

        out["accountsWithProvisionedRestoreAccess"] = (
            aws_sdk_redshift_serverless.types.account_id_list.serialize_aws_json_1_1(
                value["accounts_with_provisioned_restore_access"]
            )
        )
    if "admin_password_secret_arn" in value:
        out["adminPasswordSecretArn"] = value["admin_password_secret_arn"]
    if "admin_password_secret_kms_key_id" in value:
        out["adminPasswordSecretKmsKeyId"] = value["admin_password_secret_kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    if "namespaceName" in data:
        out["namespace_name"] = data["namespaceName"]
    if "namespaceArn" in data:
        out["namespace_arn"] = data["namespaceArn"]
    if "snapshotName" in data:
        out["snapshot_name"] = data["snapshotName"]
    if "snapshotCreateTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["snapshot_create_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["snapshotCreateTime"]
            )
        )
    if "adminUsername" in data:
        out["admin_username"] = data["adminUsername"]
    if "status" in data:
        out["status"] = data["status"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    if "ownerAccount" in data:
        out["owner_account"] = data["ownerAccount"]
    if "totalBackupSizeInMegaBytes" in data:
        out["total_backup_size_in_mega_bytes"] = data["totalBackupSizeInMegaBytes"]
    if "actualIncrementalBackupSizeInMegaBytes" in data:
        out["actual_incremental_backup_size_in_mega_bytes"] = data[
            "actualIncrementalBackupSizeInMegaBytes"
        ]
    if "backupProgressInMegaBytes" in data:
        out["backup_progress_in_mega_bytes"] = data["backupProgressInMegaBytes"]
    if "currentBackupRateInMegaBytesPerSecond" in data:
        out["current_backup_rate_in_mega_bytes_per_second"] = data[
            "currentBackupRateInMegaBytesPerSecond"
        ]
    if "estimatedSecondsToCompletion" in data:
        out["estimated_seconds_to_completion"] = data["estimatedSecondsToCompletion"]
    if "elapsedTimeInSeconds" in data:
        out["elapsed_time_in_seconds"] = data["elapsedTimeInSeconds"]
    if "snapshotRetentionPeriod" in data:
        out["snapshot_retention_period"] = data["snapshotRetentionPeriod"]
    if "snapshotRemainingDays" in data:
        out["snapshot_remaining_days"] = data["snapshotRemainingDays"]
    if "snapshotRetentionStartTime" in data:
        import aws_sdk_redshift_serverless.types._prelude.timestamp

        out["snapshot_retention_start_time"] = (
            aws_sdk_redshift_serverless.types._prelude.timestamp.deserialize_aws_json_1_1(
                data["snapshotRetentionStartTime"]
            )
        )
    if "snapshotArn" in data:
        out["snapshot_arn"] = data["snapshotArn"]
    if "accountsWithRestoreAccess" in data:
        import aws_sdk_redshift_serverless.types.account_id_list

        out["accounts_with_restore_access"] = (
            aws_sdk_redshift_serverless.types.account_id_list.deserialize_aws_json_1_1(
                data["accountsWithRestoreAccess"]
            )
        )
    if "accountsWithProvisionedRestoreAccess" in data:
        import aws_sdk_redshift_serverless.types.account_id_list

        out["accounts_with_provisioned_restore_access"] = (
            aws_sdk_redshift_serverless.types.account_id_list.deserialize_aws_json_1_1(
                data["accountsWithProvisionedRestoreAccess"]
            )
        )
    if "adminPasswordSecretArn" in data:
        out["admin_password_secret_arn"] = data["adminPasswordSecretArn"]
    if "adminPasswordSecretKmsKeyId" in data:
        out["admin_password_secret_kms_key_id"] = data["adminPasswordSecretKmsKeyId"]
    return out
