"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteFileSystemOpenZFSConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.delete_file_system_open_zfs_options
    import capo_fsx.types.flag
    import capo_fsx.types.tags


class DeleteFileSystemOpenZFSConfiguration(TypedDict, closed=True):
    skip_final_backup: NotRequired["capo_fsx.types.flag.Flag"]
    """<p>By default, Amazon FSx for OpenZFS takes a final backup on your behalf when the <code>DeleteFileSystem</code> operation is invoked. Doing this helps protect you from data loss, and we highly recommend taking the final backup. If you want to skip taking a final backup, set this value to <code>true</code>.</p>"""
    final_backup_tags: NotRequired["capo_fsx.types.tags.Tags"]
    """<p>A list of tags to apply to the file system's final backup.</p>"""
    options: NotRequired[
        "capo_fsx.types.delete_file_system_open_zfs_options.DeleteFileSystemOpenZFSOptions"
    ]
    """<p>To delete a file system if there are child volumes present below the root volume, use the string <code>DELETE_CHILD_VOLUMES_AND_SNAPSHOTS</code>. If your file system has child volumes and you don't use this option, the delete request will fail.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileSystemOpenZFSConfiguration) -> dict:
    out: dict = {}
    if "skip_final_backup" in value:
        out["SkipFinalBackup"] = value["skip_final_backup"]
    if "final_backup_tags" in value:
        import capo_fsx.types.tags

        out["FinalBackupTags"] = capo_fsx.types.tags.serialize_aws_json_1_1(
            value["final_backup_tags"]
        )
    if "options" in value:
        import capo_fsx.types.delete_file_system_open_zfs_options

        out["Options"] = (
            capo_fsx.types.delete_file_system_open_zfs_options.serialize_aws_json_1_1(
                value["options"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileSystemOpenZFSConfiguration:
    out: DeleteFileSystemOpenZFSConfiguration = {}  # type: ignore[typeddict-item]
    if "SkipFinalBackup" in data:
        out["skip_final_backup"] = data["SkipFinalBackup"]
    if "FinalBackupTags" in data:
        import capo_fsx.types.tags

        out["final_backup_tags"] = capo_fsx.types.tags.deserialize_aws_json_1_1(
            data["FinalBackupTags"]
        )
    if "Options" in data:
        import capo_fsx.types.delete_file_system_open_zfs_options

        out["options"] = (
            capo_fsx.types.delete_file_system_open_zfs_options.deserialize_aws_json_1_1(
                data["Options"]
            )
        )
    return out
