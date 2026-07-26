"""Generated from Smithy shape ``com.amazonaws.backup#ScanSetting``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.iam_role_arn
    import capo_backup.types.malware_scanner
    import capo_backup.types.resource_types


class ScanSetting(TypedDict, closed=True):
    malware_scanner: NotRequired["capo_backup.types.malware_scanner.MalwareScanner"]
    """<p>The malware scanner to use for scanning. Currently only <code>GUARDDUTY</code> is supported.</p>"""
    resource_types: NotRequired["capo_backup.types.resource_types.ResourceTypes"]
    """<p>An array of resource types to be scanned for malware.</p>"""
    scanner_role_arn: NotRequired["capo_backup.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the scanner uses to access resources; for example, <code>arn:aws:iam::123456789012:role/ScannerRole</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScanSetting) -> dict:
    out: dict = {}
    if "malware_scanner" in value:
        import capo_backup.types.malware_scanner

        out["MalwareScanner"] = capo_backup.types.malware_scanner.serialize_json(
            value["malware_scanner"]
        )
    if "resource_types" in value:
        import capo_backup.types.resource_types

        out["ResourceTypes"] = capo_backup.types.resource_types.serialize_json(
            value["resource_types"]
        )
    if "scanner_role_arn" in value:
        out["ScannerRoleArn"] = value["scanner_role_arn"]
    return out


def deserialize_json(data: dict) -> ScanSetting:
    out: ScanSetting = {}  # type: ignore[typeddict-item]
    if "MalwareScanner" in data:
        import capo_backup.types.malware_scanner

        out["malware_scanner"] = capo_backup.types.malware_scanner.deserialize_json(
            data["MalwareScanner"]
        )
    if "ResourceTypes" in data:
        import capo_backup.types.resource_types

        out["resource_types"] = capo_backup.types.resource_types.deserialize_json(
            data["ResourceTypes"]
        )
    if "ScannerRoleArn" in data:
        out["scanner_role_arn"] = data["ScannerRoleArn"]
    return out
