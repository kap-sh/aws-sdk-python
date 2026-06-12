"""Generated from Smithy shape ``com.amazonaws.migrationhub#DisassociateSourceResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.progress_update_stream
    import aws_sdk_migration_hub.types.source_resource_name


class DisassociateSourceResourceRequest(TypedDict):
    progress_update_stream: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the progress-update stream, which is used for access control as well as a namespace for migration-task names that is implicitly linked to your AWS account. The progress-update stream must uniquely identify the migration tool as it is used for all updates made by the tool; however, it does not need to be unique for each AWS account because it is scoped to the AWS account.</p>"""
    migration_task_name: (
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>A unique identifier that references the migration task. <i>Do not include sensitive data in this field.</i> </p>"""
    source_resource_name: (
        "aws_sdk_migration_hub.types.source_resource_name.SourceResourceName"
    )
    """<p>The name that was specified for the source resource.</p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>This is an optional parameter that you can use to test whether the call will succeed. Set this parameter to <code>true</code> to verify that you have the permissions that are required to make the call, and that you have specified the other parameters in the call correctly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateSourceResourceRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    out["SourceResourceName"] = value["source_resource_name"]
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateSourceResourceRequest:
    out: DisassociateSourceResourceRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "DisassociateSourceResourceRequest.progress_update_stream required"
        )
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "DisassociateSourceResourceRequest.migration_task_name required"
        )
    if "SourceResourceName" in data:
        out["source_resource_name"] = data["SourceResourceName"]
    else:
        raise DeserializationError(
            "DisassociateSourceResourceRequest.source_resource_name required"
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
