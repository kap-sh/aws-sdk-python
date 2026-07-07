"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanAdvancedBackupSettingsDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.field_map
    import aws_sdk_securityhub.types.non_empty_string


class AwsBackupBackupPlanAdvancedBackupSettingsDetails(TypedDict, closed=True):
    backup_options: NotRequired["aws_sdk_securityhub.types.field_map.FieldMap"]
    """<p>Specifies the backup option for a selected resource. This option is only available for Windows Volume Shadow Copy Service (VSS) backup jobs. Valid values are as follows:</p> <ul> <li> <p>Set to <code>WindowsVSS: enabled</code> to enable the WindowsVSS backup option and create a Windows VSS backup.</p> </li> <li> <p>Set to <code>WindowsVSS: disabled</code> to create a regular backup. The <code>WindowsVSS</code> option is not enabled by default.</p> </li> </ul>"""
    resource_type: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of a resource type. The only supported resource type is Amazon EC2 instances with Windows VSS.</p> <p>The only valid value is <code>EC2</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanAdvancedBackupSettingsDetails) -> dict:
    out: dict = {}
    if "backup_options" in value:
        import aws_sdk_securityhub.types.field_map

        out["BackupOptions"] = aws_sdk_securityhub.types.field_map.serialize_json(
            value["backup_options"]
        )
    if "resource_type" in value:
        out["ResourceType"] = value["resource_type"]
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanAdvancedBackupSettingsDetails:
    out: AwsBackupBackupPlanAdvancedBackupSettingsDetails = {}  # type: ignore[typeddict-item]
    if "BackupOptions" in data:
        import aws_sdk_securityhub.types.field_map

        out["backup_options"] = aws_sdk_securityhub.types.field_map.deserialize_json(
            data["BackupOptions"]
        )
    if "ResourceType" in data:
        out["resource_type"] = data["ResourceType"]
    return out
