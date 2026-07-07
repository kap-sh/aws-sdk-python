"""Generated from Smithy shape ``com.amazonaws.guardduty#ScannedResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.malware_protection_resource_type
    import aws_sdk_guardduty.types.malware_protection_scan_status
    import aws_sdk_guardduty.types.non_empty_string
    import aws_sdk_guardduty.types.scan_status_reason
    import aws_sdk_guardduty.types.scanned_resource_details


class ScannedResource(TypedDict, closed=True):
    scanned_resource_arn: NotRequired[
        "aws_sdk_guardduty.types.non_empty_string.NonEmptyString"
    ]
    """<p>Amazon Resource Name (ARN) of the scanned resource.</p>"""
    scanned_resource_type: NotRequired[
        "aws_sdk_guardduty.types.malware_protection_resource_type.MalwareProtectionResourceType"
    ]
    """<p>The resource type of the scanned resource.</p>"""
    scanned_resource_status: NotRequired[
        "aws_sdk_guardduty.types.malware_protection_scan_status.MalwareProtectionScanStatus"
    ]
    """<p>The status of the scanned resource.</p>"""
    scan_status_reason: NotRequired[
        "aws_sdk_guardduty.types.scan_status_reason.ScanStatusReason"
    ]
    """<p>The reason for the scan status of this particular resource, if applicable.</p>"""
    resource_details: NotRequired[
        "aws_sdk_guardduty.types.scanned_resource_details.ScannedResourceDetails"
    ]
    """<p>Information about the scanned resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScannedResource) -> dict:
    out: dict = {}
    if "scanned_resource_arn" in value:
        out["scannedResourceArn"] = value["scanned_resource_arn"]
    if "scanned_resource_type" in value:
        import aws_sdk_guardduty.types.malware_protection_resource_type

        out["scannedResourceType"] = (
            aws_sdk_guardduty.types.malware_protection_resource_type.serialize_json(
                value["scanned_resource_type"]
            )
        )
    if "scanned_resource_status" in value:
        import aws_sdk_guardduty.types.malware_protection_scan_status

        out["scannedResourceStatus"] = (
            aws_sdk_guardduty.types.malware_protection_scan_status.serialize_json(
                value["scanned_resource_status"]
            )
        )
    if "scan_status_reason" in value:
        import aws_sdk_guardduty.types.scan_status_reason

        out["scanStatusReason"] = (
            aws_sdk_guardduty.types.scan_status_reason.serialize_json(
                value["scan_status_reason"]
            )
        )
    if "resource_details" in value:
        import aws_sdk_guardduty.types.scanned_resource_details

        out["resourceDetails"] = (
            aws_sdk_guardduty.types.scanned_resource_details.serialize_json(
                value["resource_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ScannedResource:
    out: ScannedResource = {}  # type: ignore[typeddict-item]
    if "scannedResourceArn" in data:
        out["scanned_resource_arn"] = data["scannedResourceArn"]
    if "scannedResourceType" in data:
        import aws_sdk_guardduty.types.malware_protection_resource_type

        out["scanned_resource_type"] = (
            aws_sdk_guardduty.types.malware_protection_resource_type.deserialize_json(
                data["scannedResourceType"]
            )
        )
    if "scannedResourceStatus" in data:
        import aws_sdk_guardduty.types.malware_protection_scan_status

        out["scanned_resource_status"] = (
            aws_sdk_guardduty.types.malware_protection_scan_status.deserialize_json(
                data["scannedResourceStatus"]
            )
        )
    if "scanStatusReason" in data:
        import aws_sdk_guardduty.types.scan_status_reason

        out["scan_status_reason"] = (
            aws_sdk_guardduty.types.scan_status_reason.deserialize_json(
                data["scanStatusReason"]
            )
        )
    if "resourceDetails" in data:
        import aws_sdk_guardduty.types.scanned_resource_details

        out["resource_details"] = (
            aws_sdk_guardduty.types.scanned_resource_details.deserialize_json(
                data["resourceDetails"]
            )
        )
    return out
