"""Generated from Smithy shape ``com.amazonaws.guardduty#RecoveryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.continuous_scan_details
    import aws_sdk_guardduty.types.string


class RecoveryPoint(TypedDict, closed=True):
    backup_vault_name: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>The name of the Amazon Web Services Backup vault that contains the name of the recovery point to be scanned.</p>"""
    continuous_scan_details: NotRequired[
        "aws_sdk_guardduty.types.continuous_scan_details.ContinuousScanDetails"
    ]
    """<p>Contains information about the time range within the continuous backup in Amazon Web Services Backup to scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecoveryPoint) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["backupVaultName"] = value["backup_vault_name"]
    if "continuous_scan_details" in value:
        import aws_sdk_guardduty.types.continuous_scan_details

        out["continuousScanDetails"] = (
            aws_sdk_guardduty.types.continuous_scan_details.serialize_json(
                value["continuous_scan_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> RecoveryPoint:
    out: RecoveryPoint = {}  # type: ignore[typeddict-item]
    if "backupVaultName" in data:
        out["backup_vault_name"] = data["backupVaultName"]
    if "continuousScanDetails" in data:
        import aws_sdk_guardduty.types.continuous_scan_details

        out["continuous_scan_details"] = (
            aws_sdk_guardduty.types.continuous_scan_details.deserialize_json(
                data["continuousScanDetails"]
            )
        )
    return out
