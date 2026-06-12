"""Generated from Smithy shape ``com.amazonaws.migrationhub#DisassociateDiscoveredResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_migration_hub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migration_hub.types.configuration_id
    import aws_sdk_migration_hub.types.dry_run
    import aws_sdk_migration_hub.types.migration_task_name
    import aws_sdk_migration_hub.types.progress_update_stream


class DisassociateDiscoveredResourceRequest(TypedDict):
    progress_update_stream: (
        "aws_sdk_migration_hub.types.progress_update_stream.ProgressUpdateStream"
    )
    """<p>The name of the ProgressUpdateStream.</p>"""
    migration_task_name: (
        "aws_sdk_migration_hub.types.migration_task_name.MigrationTaskName"
    )
    """<p>The identifier given to the MigrationTask. <i>Do not store personal data in this field.</i> </p>"""
    configuration_id: "aws_sdk_migration_hub.types.configuration_id.ConfigurationId"
    """<p>ConfigurationId of the Application Discovery Service resource to be disassociated.</p>"""
    dry_run: "aws_sdk_migration_hub.types.dry_run.DryRun"
    """<p>Optional boolean flag to indicate whether any effect should take place. Used to test if the caller has permission to make the call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateDiscoveredResourceRequest) -> dict:
    out: dict = {}
    out["ProgressUpdateStream"] = value["progress_update_stream"]
    out["MigrationTaskName"] = value["migration_task_name"]
    out["ConfigurationId"] = value["configuration_id"]
    out["DryRun"] = value.get("dry_run", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateDiscoveredResourceRequest:
    out: DisassociateDiscoveredResourceRequest = {}  # type: ignore[typeddict-item]
    if "ProgressUpdateStream" in data:
        out["progress_update_stream"] = data["ProgressUpdateStream"]
    else:
        raise DeserializationError(
            "DisassociateDiscoveredResourceRequest.progress_update_stream required"
        )
    if "MigrationTaskName" in data:
        out["migration_task_name"] = data["MigrationTaskName"]
    else:
        raise DeserializationError(
            "DisassociateDiscoveredResourceRequest.migration_task_name required"
        )
    if "ConfigurationId" in data:
        out["configuration_id"] = data["ConfigurationId"]
    else:
        raise DeserializationError(
            "DisassociateDiscoveredResourceRequest.configuration_id required"
        )
    if "DryRun" in data:
        out["dry_run"] = data["DryRun"]
    else:
        out["dry_run"] = False
    return out
