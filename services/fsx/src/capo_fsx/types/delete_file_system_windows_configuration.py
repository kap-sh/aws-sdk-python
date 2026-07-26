"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemWindowsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.flag
    import capo_fsx.types.tags


class DeleteFileSystemWindowsConfiguration(TypedDict, closed=True):
    skip_final_backup: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>By default, Amazon FSx for Windows takes a final backup on your behalf when the <code>DeleteFileSystem</code> operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip this backup, use this flag to do so.</p>"""
    final_backup_tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>A set of tags for your final backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemWindowsConfiguration) -> dict:
    out: dict = {}
    if "skip_final_backup" in value:
        out["SkipFinalBackup"] = value["skip_final_backup"]
    if "final_backup_tags" in value:
        import capo_fsx.types.tags

        out["FinalBackupTags"] = capo_fsx.types.tags.serialize_aws_json_1_1(
            value["final_backup_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileSystemWindowsConfiguration:
    out: DeleteFileSystemWindowsConfiguration = {}  # type: ignore[typeddict-item]
    if "SkipFinalBackup" in data:
        out["skip_final_backup"] = data["SkipFinalBackup"]
    if "FinalBackupTags" in data:
        import capo_fsx.types.tags

        out["final_backup_tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(
            data["FinalBackupTags"]
        )
    return out
