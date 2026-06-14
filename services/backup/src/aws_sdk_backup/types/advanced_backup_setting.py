"""Generated from Smithy shape ``com.amazonaws.backup#AdvancedBackupSetting``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.backup_options
    import aws_sdk_backup.types.resource_type


class AdvancedBackupSetting(TypedDict):
    resource_type: NotRequired["aws_sdk_backup.types.resource_type.ResourceType"]
    r"""<p>Specifies an object containing resource type and backup options. The only supported resource type is Amazon EC2 instances with Windows Volume Shadow Copy Service (VSS). For a CloudFormation example, see the <a href=\"https://docs.aws.amazon.com/aws-backup/latest/devguide/integrate-cloudformation-with-aws-backup.html\">sample CloudFormation template to enable Windows VSS</a> in the <i>Backup User Guide</i>.</p> <p>Valid values: <code>EC2</code>.</p>"""
    backup_options: NotRequired["aws_sdk_backup.types.backup_options.BackupOptions"]
    r"""<p>Specifies the backup option for a selected resource. This option is available for Windows VSS backup jobs and S3 backups.</p> <p>Valid values: </p> <p>Set to <code>\"WindowsVSS\":\"enabled\"</code> to enable the <code>WindowsVSS</code> backup option and create a Windows VSS backup. </p> <p>Set to <code>\"WindowsVSS\":\"disabled\"</code> to create a regular backup. The <code>WindowsVSS</code> option is not enabled by default.</p> <p>For S3 backups, set to <code>\"BackupACLs\":\"disabled\"</code> to exclude ACLs from the backup, or <code>\"BackupObjectTags\":\"disabled\"</code> to exclude object tags from the backup. By default, both ACLs and object tags are included in S3 backups.</p> <p>If you specify an invalid option, you get an <code>InvalidParameterValueException</code> exception.</p> <p>For more information about Windows VSS backups, see <a href=\"https://docs.aws.amazon.com/aws-backup/latest/devguide/windows-backups.html\">Creating a VSS-Enabled Windows Backup</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedBackupSetting) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    if "backup_options" in value:
        import aws_sdk_backup.types.backup_options

        out["BackupOptions"] = aws_sdk_backup.types.backup_options.serialize_json(
            value["backup_options"]
        )
    return out


def deserialize_json(data: dict) -> AdvancedBackupSetting:
    out: AdvancedBackupSetting = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    if "BackupOptions" in data:
        import aws_sdk_backup.types.backup_options

        out["backup_options"] = aws_sdk_backup.types.backup_options.deserialize_json(
            data["BackupOptions"]
        )
    return out
