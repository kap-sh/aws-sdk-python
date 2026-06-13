"""Generated from Smithy shape ``com.amazonaws.backupsearch#S3ResultItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.object_key


class S3ResultItem(TypedDict):
    backup_resource_arn: NotRequired["str"]
    """<p>These are items in the returned results that match recovery point Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.</p>"""
    source_resource_arn: NotRequired["str"]
    """<p>These are items in the returned results that match source Amazon Resource Names (ARN) input during a search of Amazon S3 backup metadata.</p>"""
    backup_vault_name: NotRequired["str"]
    """<p>The name of the backup vault.</p>"""
    object_key: NotRequired["aws_sdk_backupsearch.types.object_key.ObjectKey"]
    """<p>This is one or more items returned in the results of a search of Amazon S3 backup metadata that match the values input for object key.</p>"""
    object_size: NotRequired["int"]
    """<p>These are items in the returned results that match values for object size(s) input during a search of Amazon S3 backup metadata.</p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p>These are one or more items in the returned results that match values for item creation time input during a search of Amazon S3 backup metadata.</p>"""
    e_tag: NotRequired["str"]
    """<p>These are one or more items in the returned results that match values for ETags input during a search of Amazon S3 backup metadata.</p>"""
    version_id: NotRequired["str"]
    """<p>These are one or more items in the returned results that match values for version IDs input during a search of Amazon S3 backup metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3ResultItem) -> dict:
    out: dict = {}
    if "backup_resource_arn" in value:
        out["BackupResourceArn"] = value["backup_resource_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "object_key" in value:
        out["ObjectKey"] = value["object_key"]
    if "object_size" in value:
        out["ObjectSize"] = value["object_size"]
    if "creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["CreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["creation_time"]
            )
        )
    if "e_tag" in value:
        out["ETag"] = value["e_tag"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    return out


def deserialize_json(data: dict) -> S3ResultItem:
    out: S3ResultItem = {}  # type: ignore[typeddict-item]
    if "BackupResourceArn" in data:
        out["backup_resource_arn"] = data["BackupResourceArn"]
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "ObjectKey" in data:
        out["object_key"] = data["ObjectKey"]
    if "ObjectSize" in data:
        out["object_size"] = data["ObjectSize"]
    if "CreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    if "ETag" in data:
        out["e_tag"] = data["ETag"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    return out
