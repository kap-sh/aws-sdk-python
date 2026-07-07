"""Generated from Smithy shape ``com.amazonaws.backup#RecoveryPointSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_backup.types.date_range
    import aws_sdk_backup.types.resource_identifiers
    import aws_sdk_backup.types.vault_names


class RecoveryPointSelection(TypedDict, closed=True):
    vault_names: NotRequired["aws_sdk_backup.types.vault_names.VaultNames"]
    """<p>These are the names of the vaults in which the selected recovery points are contained.</p>"""
    resource_identifiers: NotRequired[
        "aws_sdk_backup.types.resource_identifiers.ResourceIdentifiers"
    ]
    """<p>These are the resources included in the resource selection (including type of resources and vaults).</p>"""
    date_range: NotRequired["aws_sdk_backup.types.date_range.DateRange"]


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointSelection) -> dict:
    out: dict = {}
    if "vault_names" in value:
        import aws_sdk_backup.types.vault_names

        out["VaultNames"] = aws_sdk_backup.types.vault_names.serialize_json(
            value["vault_names"]
        )
    if "resource_identifiers" in value:
        import aws_sdk_backup.types.resource_identifiers

        out["ResourceIdentifiers"] = (
            aws_sdk_backup.types.resource_identifiers.serialize_json(
                value["resource_identifiers"]
            )
        )
    if "date_range" in value:
        import aws_sdk_backup.types.date_range

        out["DateRange"] = aws_sdk_backup.types.date_range.serialize_json(
            value["date_range"]
        )
    return out


def deserialize_json(data: dict) -> RecoveryPointSelection:
    out: RecoveryPointSelection = {}  # type: ignore[typeddict-item]
    if "VaultNames" in data:
        import aws_sdk_backup.types.vault_names

        out["vault_names"] = aws_sdk_backup.types.vault_names.deserialize_json(
            data["VaultNames"]
        )
    if "ResourceIdentifiers" in data:
        import aws_sdk_backup.types.resource_identifiers

        out["resource_identifiers"] = (
            aws_sdk_backup.types.resource_identifiers.deserialize_json(
                data["ResourceIdentifiers"]
            )
        )
    if "DateRange" in data:
        import aws_sdk_backup.types.date_range

        out["date_range"] = aws_sdk_backup.types.date_range.deserialize_json(
            data["DateRange"]
        )
    return out
