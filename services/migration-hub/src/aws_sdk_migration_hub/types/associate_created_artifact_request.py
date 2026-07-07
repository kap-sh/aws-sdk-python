"""Generated from Smithy shape ``com.amazonaws.migrationhub#AssociateCreatedArtifactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.created_artifact
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.progress_update_stream


class AssociateCreatedArtifactRequest(TypedDict, closed=True):
    progress_update_stream: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream. </p>"""
    migration_task_name: (
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>Unique identifier that references the migration task. <i>Do not store personal data in this field.</i> </p>"""
    created_artifact: "aws_sdk_migration_hub.types.created_artifact.CreatedArtifact"
    """<p>An ARN of the AWS resource related to the migration (e.g., AMI, EC2 instance, RDS instance, etc.) </p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateCreatedArtifactRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    import aws_sdk_migration_hub.types.created_artifact

    out["CreatedArtifact"] = (
        aws_sdk_migration_hub.types.created_artifact.serialize_aws_json_1_1(
            value["created_artifact"]
        )
    )
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateCreatedArtifactRequest:
    out: AssociateCreatedArtifactRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "AssociateCreatedArtifactRequest.progress_update_stream required"
        )
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "AssociateCreatedArtifactRequest.migration_task_name required"
        )
    if "CreatedArtifact" in data:
        import aws_sdk_migration_hub.types.created_artifact

        out["created_artifact"] = (
            aws_sdk_migration_hub.types.created_artifact.deserialize_aws_json_1_1(
                data["CreatedArtifact"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateCreatedArtifactRequest.created_artifact required"
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
