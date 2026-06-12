"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#DestinationLogsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.log_group_name_configuration
    import aws_sdk_observabilityadmin.types.logs_backup_configuration
    import aws_sdk_observabilityadmin.types.logs_encryption_configuration


class DestinationLogsConfiguration(TypedDict):
    logs_encryption_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.logs_encryption_configuration.LogsEncryptionConfiguration"
    ]
    """<p>The encryption configuration for centralization destination log groups.</p>"""
    backup_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.logs_backup_configuration.LogsBackupConfiguration"
    ]
    """<p>Configuration defining the backup region and an optional KMS key for the backup destination.</p>"""
    log_group_name_configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.log_group_name_configuration.LogGroupNameConfiguration"
    ]
    """<p>Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationLogsConfiguration) -> dict:
    out: dict = {}
    if "logs_encryption_configuration" in value:
        import aws_sdk_observabilityadmin.types.logs_encryption_configuration

        out["LogsEncryptionConfiguration"] = (
            aws_sdk_observabilityadmin.types.logs_encryption_configuration.serialize_json(
                value["logs_encryption_configuration"]
            )
        )
    if "backup_configuration" in value:
        import aws_sdk_observabilityadmin.types.logs_backup_configuration

        out["BackupConfiguration"] = (
            aws_sdk_observabilityadmin.types.logs_backup_configuration.serialize_json(
                value["backup_configuration"]
            )
        )
    if "log_group_name_configuration" in value:
        import aws_sdk_observabilityadmin.types.log_group_name_configuration

        out["LogGroupNameConfiguration"] = (
            aws_sdk_observabilityadmin.types.log_group_name_configuration.serialize_json(
                value["log_group_name_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DestinationLogsConfiguration:
    out: DestinationLogsConfiguration = {}  # type: ignore[typeddict-item]
    if "LogsEncryptionConfiguration" in data:
        import aws_sdk_observabilityadmin.types.logs_encryption_configuration

        out["logs_encryption_configuration"] = (
            aws_sdk_observabilityadmin.types.logs_encryption_configuration.deserialize_json(
                data["LogsEncryptionConfiguration"]
            )
        )
    if "BackupConfiguration" in data:
        import aws_sdk_observabilityadmin.types.logs_backup_configuration

        out["backup_configuration"] = (
            aws_sdk_observabilityadmin.types.logs_backup_configuration.deserialize_json(
                data["BackupConfiguration"]
            )
        )
    if "LogGroupNameConfiguration" in data:
        import aws_sdk_observabilityadmin.types.log_group_name_configuration

        out["log_group_name_configuration"] = (
            aws_sdk_observabilityadmin.types.log_group_name_configuration.deserialize_json(
                data["LogGroupNameConfiguration"]
            )
        )
    return out
