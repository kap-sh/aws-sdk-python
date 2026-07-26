"""Generated from Smithy shape ``com.amazonaws.guardduty#ScanConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.incremental_scan_details
    import capo_guardduty.types.non_empty_string
    import capo_guardduty.types.scan_configuration_recovery_point
    import capo_guardduty.types.trigger_details


class ScanConfiguration(TypedDict, closed=True):
    role: NotRequired["capo_guardduty.types.non_empty_string.NonEmptyString"]
    """<p>Amazon Resource Name (ARN) of the IAM role that should contain the required permissions for the scan.</p>"""
    trigger_details: NotRequired["capo_guardduty.types.trigger_details.TriggerDetails"]
    """<p>Information about the entity that triggered the malware scan.</p>"""
    incremental_scan_details: NotRequired[
        "capo_guardduty.types.incremental_scan_details.IncrementalScanDetails"
    ]
    """<p>Information about the incremental scan configuration, if applicable.</p>"""
    recovery_point: NotRequired[
        "capo_guardduty.types.scan_configuration_recovery_point.ScanConfigurationRecoveryPoint"
    ]
    """<p>Information about the recovery point configuration used for the scan, if applicable.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanConfiguration) -> dict:
    out: dict = {}
    if "role" in value:
        out["role"] = value["role"]
    if "trigger_details" in value:
        import capo_guardduty.types.trigger_details

        out["triggerDetails"] = capo_guardduty.types.trigger_details.serialize_json(
            value["trigger_details"]
        )
    if "incremental_scan_details" in value:
        import capo_guardduty.types.incremental_scan_details

        out["incrementalScanDetails"] = (
            capo_guardduty.types.incremental_scan_details.serialize_json(
                value["incremental_scan_details"]
            )
        )
    if "recovery_point" in value:
        import capo_guardduty.types.scan_configuration_recovery_point

        out["recoveryPoint"] = (
            capo_guardduty.types.scan_configuration_recovery_point.serialize_json(
                value["recovery_point"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScanConfiguration:
    out: ScanConfiguration = {}  # type: ignore[typeddict-item]
    if "role" in data:
        out["role"] = data["role"]
    if "triggerDetails" in data:
        import capo_guardduty.types.trigger_details

        out["trigger_details"] = capo_guardduty.types.trigger_details.deserialize_json(
            data["triggerDetails"]
        )
    if "incrementalScanDetails" in data:
        import capo_guardduty.types.incremental_scan_details

        out["incremental_scan_details"] = (
            capo_guardduty.types.incremental_scan_details.deserialize_json(
                data["incrementalScanDetails"]
            )
        )
    if "recoveryPoint" in data:
        import capo_guardduty.types.scan_configuration_recovery_point

        out["recovery_point"] = (
            capo_guardduty.types.scan_configuration_recovery_point.deserialize_json(
                data["recoveryPoint"]
            )
        )
    return out
