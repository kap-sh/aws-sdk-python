"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanConfigurationRecoveryPoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.non_empty_string
    import aws_sdk_guardduty.types.scan_configuration_continuous_scan_details


class ScanConfigurationRecoveryPoint(TypedDict, closed=True):
    backup_vault_name: NotRequired[
        "aws_sdk_guardduty.types.non_empty_string.NonEmptyString"
    ]
    """<p>The name of the Amazon Web Services Backup vault that contains the recovery point for the scanned.</p>"""
    continuous_scan_details: NotRequired[
        "aws_sdk_guardduty.types.scan_configuration_continuous_scan_details.ScanConfigurationContinuousScanDetails"
    ]
    """<p>The time range within the continuous backup in Amazon Web Services Backup that was scanned for a point-in-time recovery resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanConfigurationRecoveryPoint) -> dict:
    out: dict = {}
    if "backup_vault_name" in value:
        out["backupVaultName"] = value["backup_vault_name"]
    if "continuous_scan_details" in value:
        import aws_sdk_guardduty.types.scan_configuration_continuous_scan_details

        out["continuousScanDetails"] = (
            aws_sdk_guardduty.types.scan_configuration_continuous_scan_details.serialize_json(
                value["continuous_scan_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScanConfigurationRecoveryPoint:
    out: ScanConfigurationRecoveryPoint = {}  # type: ignore[typeddict-item]
    if "backupVaultName" in data:
        out["backup_vault_name"] = data["backupVaultName"]
    if "continuousScanDetails" in data:
        import aws_sdk_guardduty.types.scan_configuration_continuous_scan_details

        out["continuous_scan_details"] = (
            aws_sdk_guardduty.types.scan_configuration_continuous_scan_details.deserialize_json(
                data["continuousScanDetails"]
            )
        )
    return out
