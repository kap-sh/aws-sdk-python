"""Generated from Smithy shape ``com.amazonaws.guardduty#RecoveryPointDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.string


class RecoveryPointDetails(TypedDict):
    recovery_point_arn: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the recovery point.</p>"""
    backup_vault_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the backup vault containing the recovery point.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPointDetails) -> dict:
    out: dict = {}
    if "recovery_point_arn" in value:
        out["recoveryPointArn"] = value["recovery_point_arn"]
    if "backup_vault_name" in value:
        out["backupVaultName"] = value["backup_vault_name"]
    return out


def deserialize_json(data: dict) -> RecoveryPointDetails:
    out: RecoveryPointDetails = {}  # type: ignore[typeddict-item]
    if "recoveryPointArn" in data:
        out["recovery_point_arn"] = data["recoveryPointArn"]
    if "backupVaultName" in data:
        out["backup_vault_name"] = data["backupVaultName"]
    return out
