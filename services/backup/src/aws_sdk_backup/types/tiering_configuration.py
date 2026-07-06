"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_backup.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_backup.types.arn
    import aws_sdk_backup.types.backup_vault_name_or_wildcard
    import aws_sdk_backup.types.creator_request_id
    import aws_sdk_backup.types.resource_selections
    import aws_sdk_backup.types.tiering_configuration_name
    import aws_sdk_backup.types.timestamp


class TieringConfiguration(TypedDict, closed=True):
    tiering_configuration_name: (
        "aws_sdk_backup.types.tiering_configuration_name.TieringConfigurationName"
    )
    """<p>The unique name of the tiering configuration. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.</p>"""
    tiering_configuration_arn: NotRequired["aws_sdk_backup.types.arn.ARN"]
    """<p>An Amazon Resource Name (ARN) that uniquely identifies the tiering configuration.</p>"""
    backup_vault_name: (
        "aws_sdk_backup.types.backup_vault_name_or_wildcard.BackupVaultNameOrWildcard"
    )
    """<p>The name of the backup vault where the tiering configuration applies. Use <code>*</code> to apply to all backup vaults.</p>"""
    resource_selection: "aws_sdk_backup.types.resource_selections.ResourceSelections"
    """<p>An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.</p>"""
    creator_request_id: NotRequired[
        "aws_sdk_backup.types.creator_request_id.CreatorRequestId"
    ]
    """<p>This is a unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.</p>"""
    creation_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was created, in Unix format and Coordinated Universal Time (UTC). The value of <code>CreationTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""
    last_updated_time: NotRequired["aws_sdk_backup.types.timestamp.timestamp"]
    """<p>The date and time a tiering configuration was updated, in Unix format and Coordinated Universal Time (UTC). The value of <code>LastUpdatedTime</code> is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfiguration) -> dict:
    out: dict = {}
    out["TieringConfigurationName"] = value["tiering_configuration_name"]
    if "tiering_configuration_arn" in value:
        out["TieringConfigurationArn"] = value["tiering_configuration_arn"]
    out["BackupVaultName"] = value["backup_vault_name"]
    import aws_sdk_backup.types.resource_selections

    out["ResourceSelection"] = aws_sdk_backup.types.resource_selections.serialize_json(
        value["resource_selection"]
    )
    if "creator_request_id" in value:
        out["CreatorRequestId"] = value["creator_request_id"]
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


def deserialize_json(data: dict) -> TieringConfiguration:
    out: TieringConfiguration = {}  # type: ignore[typeddict-item]
    if "TieringConfigurationName" in data:
        out["tiering_configuration_name"] = data["TieringConfigurationName"]
    else:
        raise DeserializationError(
            "TieringConfiguration.tiering_configuration_name required"
        )
    if "TieringConfigurationArn" in data:
        out["tiering_configuration_arn"] = data["TieringConfigurationArn"]
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        raise DeserializationError("TieringConfiguration.backup_vault_name required")
    if "ResourceSelection" in data:
        import aws_sdk_backup.types.resource_selections

        out["resource_selection"] = (
            aws_sdk_backup.types.resource_selections.deserialize_json(
                data["ResourceSelection"]
            )
        )
    else:
        raise DeserializationError("TieringConfiguration.resource_selection required")
    if "CreatorRequestId" in data:
        out["creator_request_id"] = data["CreatorRequestId"]
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
