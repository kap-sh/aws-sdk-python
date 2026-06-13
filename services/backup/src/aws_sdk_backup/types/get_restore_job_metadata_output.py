"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreJobMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.metadata
    import aws_sdk_backup.types.restore_job_id


class GetRestoreJobMetadataOutput(TypedDict):
    restore_job_id: NotRequired["aws_sdk_backup.types.restore_job_id.RestoreJobId"]
    """<p>This is a unique identifier of a restore job within Backup.</p>"""
    metadata: NotRequired["aws_sdk_backup.types.metadata.Metadata"]
    """<p>This contains the metadata of the specified backup job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreJobMetadataOutput) -> dict:
    out: dict = {}
    if "restore_job_id" in value:
        out["RestoreJobId"] = value["restore_job_id"]
    if "metadata" in value:
        import aws_sdk_backup.types.metadata

        out["Metadata"] = aws_sdk_backup.types.metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> GetRestoreJobMetadataOutput:
    out: GetRestoreJobMetadataOutput = {}  # type: ignore[typeddict-item]
    if "RestoreJobId" in data:
        out["restore_job_id"] = data["RestoreJobId"]
    if "Metadata" in data:
        import aws_sdk_backup.types.metadata

        out["metadata"] = aws_sdk_backup.types.metadata.deserialize_json(
            data["Metadata"]
        )
    return out
