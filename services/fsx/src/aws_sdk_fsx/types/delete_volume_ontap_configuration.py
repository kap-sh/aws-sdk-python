"""Generated from Smithy shape ``com.amazonaws.fsx#DeleteVolumeOntapConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.flag
    import aws_sdk_fsx.types.tags


class DeleteVolumeOntapConfiguration(TypedDict):
    skip_final_backup: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    """<p>Set to true if you want to skip taking a final backup of the volume you are deleting.</p>"""
    final_backup_tags: NotRequired["aws_sdk_fsx.types.tags.Tags"]
    bypass_snaplock_enterprise_retention: NotRequired["aws_sdk_fsx.types.flag.Flag"]
    r"""<p>Setting this to <code>true</code> allows a SnapLock administrator to delete an FSx for ONTAP SnapLock Enterprise volume with unexpired write once, read many (WORM) files. The IAM permission <code>fsx:BypassSnaplockEnterpriseRetention</code> is also required to delete SnapLock Enterprise volumes with unexpired WORM files. The default value is <code>false</code>. </p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/snaplock-delete-volume.html\"> Deleting a SnapLock volume</a>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteVolumeOntapConfiguration) -> dict:
    out: dict = {}
    if "skip_final_backup" in value:
        out["SkipFinalBackup"] = value["skip_final_backup"]
    if "final_backup_tags" in value:
        import aws_sdk_fsx.types.tags

        out["FinalBackupTags"] = aws_sdk_fsx.types.tags.serialize_aws_json_1_1(
            value["final_backup_tags"]
        )
    if "bypass_snaplock_enterprise_retention" in value:
        out["BypassSnaplockEnterpriseRetention"] = value[
            "bypass_snaplock_enterprise_retention"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteVolumeOntapConfiguration:
    out: DeleteVolumeOntapConfiguration = {}  # type: ignore[typeddict-item]
    if "SkipFinalBackup" in data:
        out["skip_final_backup"] = data["SkipFinalBackup"]
    if "FinalBackupTags" in data:
        import aws_sdk_fsx.types.tags

        out["final_backup_tags"] = aws_sdk_fsx.types.tags.deserialize_aws_json_1_1(
            data["FinalBackupTags"]
        )
    if "BypassSnaplockEnterpriseRetention" in data:
        out["bypass_snaplock_enterprise_retention"] = data[
            "BypassSnaplockEnterpriseRetention"
        ]
    return out
