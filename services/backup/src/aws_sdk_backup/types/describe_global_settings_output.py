"""Generated from Smithy shape ``com.amazonaws.backup#DescribeGlobalSettingsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.global_settings
    import aws_sdk_backup.types.timestamp


class DescribeGlobalSettingsOutput(TypedDict):
    global_settings: NotRequired["aws_sdk_backup.types.global_settings.GlobalSettings"]
    """<p>The status of the flags <code>isCrossAccountBackupEnabled</code>, <code>isMpaEnabled</code> ('Mpa' refers to multi-party approval), and <code>isDelegatedAdministratorEnabled</code>.</p> <ul> <li> <p> <code>isCrossAccountBackupEnabled</code>: Allow accounts in your organization to copy backups to other accounts.</p> </li> <li> <p> <code>isMpaEnabled</code>: Add cross-account access to your organization with the option to assign a Multi-party approval team to a logically air-gapped vault.</p> </li> <li> <p> <code>isDelegatedAdministratorEnabled</code>: Allow Backup to automatically synchronize delegated administrator permissions with Organizations.</p> </li> </ul>"""
    last_update_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time that the supported flags were last updated. This update is in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdateTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGlobalSettingsOutput) -> dict:
    out: dict = {}
    if "global_settings" in value:
        import aws_sdk_backup.types.global_settings

        out["GlobalSettings"] = aws_sdk_backup.types.global_settings.serialize_json(
            value["global_settings"]
        )
    if "last_update_time" in value:
        import aws_sdk_backup.types.timestamp

        out["LastUpdateTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["last_update_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeGlobalSettingsOutput:
    out: DescribeGlobalSettingsOutput = {}  # type: ignore[typeddict-item]
    if "GlobalSettings" in data:
        import aws_sdk_backup.types.global_settings

        out["global_settings"] = aws_sdk_backup.types.global_settings.deserialize_json(
            data["GlobalSettings"]
        )
    if "LastUpdateTime" in data:
        import aws_sdk_backup.types.timestamp

        out["last_update_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["LastUpdateTime"]
        )
    return out
