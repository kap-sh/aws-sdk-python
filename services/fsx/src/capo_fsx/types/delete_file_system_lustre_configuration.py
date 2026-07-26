"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemLustreConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.flag
    import capo_fsx.types.tags


class DeleteFileSystemLustreConfiguration(TypedDict, closed=True):
    skip_final_backup: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>Set <code>SkipFinalBackup</code> to false if you want to take a final backup of the file system you are deleting. By default, Amazon FSx will not take a final backup on your behalf when the <code>DeleteFileSystem</code> operation is invoked. (Default = true)</p> <note> <p>The <code>fsx:CreateBackup</code> permission is required if you set <code>SkipFinalBackup</code> to <code>false</code> in order to delete the file system and take a final backup.</p> </note>"""
    final_backup_tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>Use if <code>SkipFinalBackup</code> is set to <code>false</code>, and you want to apply an array of tags to the final backup. If you have set the file system property <code>CopyTagsToBackups</code> to true, and you specify one or more <code>FinalBackupTags</code> when deleting a file system, Amazon FSx will not copy any existing file system tags to the backup.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemLustreConfiguration) -> dict:
    out: dict = {}
    if "skip_final_backup" in value:
        out["SkipFinalBackup"] = value["skip_final_backup"]
    if "final_backup_tags" in value:
        import capo_fsx.types.tags

        out["FinalBackupTags"] = capo_fsx.types.tags.serialize_aws_json_1_1(
            value["final_backup_tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileSystemLustreConfiguration:
    out: DeleteFileSystemLustreConfiguration = {}  # type: ignore[typeddict-item]
    if "SkipFinalBackup" in data:
        out["skip_final_backup"] = data["SkipFinalBackup"]
    if "FinalBackupTags" in data:
        import capo_fsx.types.tags

        out["final_backup_tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(
            data["FinalBackupTags"]
        )
    return out
