"""Generated from Smithy shape ``com.amazonaws.backupsearch#SearchJobBackupsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_backupsearch.types.resource_type
    import aws_sdk_backupsearch.types.search_job_state


class SearchJobBackupsResult(TypedDict):
    status: NotRequired["aws_sdk_backupsearch.types.search_job_state.SearchJobState"]
    """<p>This is the status of the search job backup result.</p>"""
    status_message: NotRequired["str"]
    """<p>This is the status message included with the results.</p>"""
    resource_type: NotRequired["aws_sdk_backupsearch.types.resource_type.ResourceType"]
    """<p>This is the resource type of the search.</p>"""
    backup_resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the backup resources.</p>"""
    source_resource_arn: NotRequired["str"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the source resources.</p>"""
    index_creation_time: NotRequired["datetime.datetime"]
    """<p>This is the creation time of the backup index.</p>"""
    backup_creation_time: NotRequired["datetime.datetime"]
    """<p>This is the creation time of the backup (recovery point).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchJobBackupsResult) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_backupsearch.types.search_job_state

        out["Status"] = aws_sdk_backupsearch.types.search_job_state.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    if "resource_type" in value:
        import aws_sdk_backupsearch.types.resource_type

        out["ResourceType"] = aws_sdk_backupsearch.types.resource_type.serialize_json(
            value["resource_type"]
        )
    if "backup_resource_arn" in value:
        out["BackupResourceArn"] = value["backup_resource_arn"]
    if "source_resource_arn" in value:
        out["SourceResourceArn"] = value["source_resource_arn"]
    if "index_creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["IndexCreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["index_creation_time"]
            )
        )
    if "backup_creation_time" in value:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["BackupCreationTime"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.serialize_json(
                value["backup_creation_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchJobBackupsResult:
    out: SearchJobBackupsResult = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_backupsearch.types.search_job_state

        out["status"] = aws_sdk_backupsearch.types.search_job_state.deserialize_json(
            data["Status"]
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    if "ResourceType" in data:
        import aws_sdk_backupsearch.types.resource_type

        out["resource_type"] = (
            aws_sdk_backupsearch.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if "BackupResourceArn" in data:
        out["backup_resource_arn"] = data["BackupResourceArn"]
    if "SourceResourceArn" in data:
        out["source_resource_arn"] = data["SourceResourceArn"]
    if "IndexCreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["index_creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["IndexCreationTime"]
            )
        )
    if "BackupCreationTime" in data:
        import aws_sdk_backupsearch.types._prelude.timestamp

        out["backup_creation_time"] = (
            aws_sdk_backupsearch.types._prelude.timestamp.deserialize_json(
                data["BackupCreationTime"]
            )
        )
    return out
