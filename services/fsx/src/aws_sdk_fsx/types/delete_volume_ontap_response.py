"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteVolumeOntapResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.backup_id
    import aws_sdk_fsx.types.tags


class DeleteVolumeOntapResponse(TypedDict, closed=True):
    final_backup_id: NotRequired["aws_sdk_fsx.types.backup_id.BackupId"]
    final_backup_tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeOntapResponse) -> dict:
    out: dict = {}
    if "final_backup_id" in value:
        out["FinalBackupId"] = value["final_backup_id"]
    if "final_backup_tags" in value:
        import aws_sdk_fsx.types.tags

        out["FinalBackupTags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(
            value["final_backup_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeOntapResponse:
    out: DeleteVolumeOntapResponse = {}  # type: ignore[typeddict-item]
    if "FinalBackupId" in data:
        out["final_backup_id"] = data["FinalBackupId"]
    if "FinalBackupTags" in data:
        import aws_sdk_fsx.types.tags

        out["final_backup_tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(
            data["FinalBackupTags"]
        )
    return out
