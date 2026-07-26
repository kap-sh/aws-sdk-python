"""Generated from Smithy shape ``com.amazonaws.backup#TieringConfigurationInputForUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_backup.errors import DeserializationError

if TYPE_CHECKING:
    import capo_backup.types.backup_vault_name_or_wildcard
    import capo_backup.types.resource_selections


class TieringConfigurationInputForUpdate(TypedDict, closed=True):
    resource_selection: "capo_backup.types.resource_selections.ResourceSelections"
    """<p>An array of resource selection objects that specify which resources are included in the tiering configuration and their tiering settings.</p>"""
    backup_vault_name: (
        "capo_backup.types.backup_vault_name_or_wildcard.BackupVaultNameOrWildcard"
    )
    """<p>The name of the backup vault where the tiering configuration applies. Use <code>*</code> to apply to all backup vaults.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TieringConfigurationInputForUpdate) -> dict:
    out: dict = {}
    import capo_backup.types.resource_selections

    out["ResourceSelection"] = capo_backup.types.resource_selections.serialize_json(
        value["resource_selection"]
    )
    out["BackupVaultName"] = value["backup_vault_name"]
    return out


def deserialize_json(data: dict) -> TieringConfigurationInputForUpdate:
    out: TieringConfigurationInputForUpdate = {}  # type: ignore[typeddict-item]
    if "ResourceSelection" in data:
        import capo_backup.types.resource_selections

        out["resource_selection"] = (
            capo_backup.types.resource_selections.deserialize_json(
                data["ResourceSelection"]
            )
        )
    else:
        raise DeserializationError(
            "TieringConfigurationInputForUpdate.resource_selection required"
        )
    if "BackupVaultName" in data:
        out["backup_vault_name"] = data["BackupVaultName"]
    else:
        raise DeserializationError(
            "TieringConfigurationInputForUpdate.backup_vault_name required"
        )
    return out
