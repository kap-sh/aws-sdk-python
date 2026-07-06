"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfigurationsListMember``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name_or_wildcard
    import aws_sdk_backup.types.tiering_configuration_name
    import aws_sdk_backup.types.timestamp


class TieringConfigurationsListMember(TypedDict, closed=True):
    tiering_configuration_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.</p>"""
    tiering_configuration_name: NotRequired[
        "aws_sdk_backup.types.tiering_configuration_name.TieringConfigurationName"
    ]
    """<p>The unique name of the tiering configuration.</p>"""
    backup_vault_name: NotRequired[
        "aws_sdk_backup.types.backup_vault_name_or_wildcard.BackupVaultNameOrWildcard"
    ]
    """<p>The name of the backup vault where the tiering configuration applies. Use <code>*</code> to apply to all backup vaults.</p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""
    last_updated_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdatedTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfigurationsListMember) -> dict:
    out: dict = {}
    if "tiering_configuration_arn" in value:
        out["TieringConfigurationArn"] = value["tiering_configuration_arn"]
    if "tiering_configuration_name" in value:
        out["TieringConfigurationName"] = value["tiering_configuration_name"]
    if "backup_vault_name" in value:
        out["BackupVaultName"] = value["backup_vault_name"]
    if "creation_time" in value:
        import aws_sdk_backup.types.timestamp

        out["CreationTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_backup.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_backup.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> TieringConfigurationsListMember:
    out: TieringConfigurationsListMember = {}  # type: ignore[typeddict-item]
    if "TieringConfigurationArn" in data:
        out["tiering_configuration_arn"] = data["TieringConfigurationArn"]
    if "TieringConfigurationName" in data:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    if "CreationTime" in data:
        import aws_sdk_backup.types.timestamp

        out["creation_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_backup.types.timestamp

        out["last_updated_time"] = aws_sdk_backup.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    return out
