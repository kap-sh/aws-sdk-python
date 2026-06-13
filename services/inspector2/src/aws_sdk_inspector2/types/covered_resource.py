"""Generated from Smithy shape ``com.amazonaws.inspector2#CoveredResource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.account_id
    import aws_sdk_inspector2.types.coverage_resource_type
    import aws_sdk_inspector2.types.date_time_timestamp
    import aws_sdk_inspector2.types.resource_id
    import aws_sdk_inspector2.types.resource_scan_metadata
    import aws_sdk_inspector2.types.scan_mode
    import aws_sdk_inspector2.types.scan_status
    import aws_sdk_inspector2.types.scan_type


class CoveredResource(TypedDict):
    resource_type: (
        "aws_sdk_inspector2.types.coverage_resource_type.CoverageResourceType"
    )
    """<p>The type of the covered resource.</p>"""
    resource_id: "aws_sdk_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the covered resource.</p>"""
    account_id: "aws_sdk_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the covered resource.</p>"""
    scan_type: "aws_sdk_inspector2.types.scan_type.ScanType"
    """<p>The Amazon Inspector scan type covering the resource.</p>"""
    scan_status: NotRequired["aws_sdk_inspector2.types.scan_status.ScanStatus"]
    """<p>The status of the scan covering the resource.</p>"""
    resource_metadata: NotRequired[
        "aws_sdk_inspector2.types.resource_scan_metadata.ResourceScanMetadata"
    ]
    """<p>An object that contains details about the metadata.</p>"""
    last_scanned_at: NotRequired[
        "aws_sdk_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the resource was last checked for vulnerabilities.</p>"""
    scan_mode: NotRequired["aws_sdk_inspector2.types.scan_mode.ScanMode"]
    """<p>The scan method that is applied to the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoveredResource) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resourceId"] = value["resource_id"]
    out["accountId"] = value["account_id"]
    out["scanType"] = value["scan_type"]
    if "scan_status" in value:
        import aws_sdk_inspector2.types.scan_status

        out["scanStatus"] = aws_sdk_inspector2.types.scan_status.serialize_json(
            value["scan_status"]
        )
    if "resource_metadata" in value:
        import aws_sdk_inspector2.types.resource_scan_metadata

        out["resourceMetadata"] = (
            aws_sdk_inspector2.types.resource_scan_metadata.serialize_json(
                value["resource_metadata"]
            )
        )
    if "last_scanned_at" in value:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["lastScannedAt"] = (
            aws_sdk_inspector2.types.date_time_timestamp.serialize_json(
                value["last_scanned_at"]
            )
        )
    if "scan_mode" in value:
        out["scanMode"] = value["scan_mode"]
    return out


def deserialize_json(data: dict) -> CoveredResource:
    out: CoveredResource = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("CoveredResource.resource_type required")
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    else:
        raise DeserializationError("CoveredResource.resource_id required")
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    else:
        raise DeserializationError("CoveredResource.account_id required")
    if "scanType" in data:
        out["scan_type"] = data["scanType"]
    else:
        raise DeserializationError("CoveredResource.scan_type required")
    if "scanStatus" in data:
        import aws_sdk_inspector2.types.scan_status

        out["scan_status"] = aws_sdk_inspector2.types.scan_status.deserialize_json(
            data["scanStatus"]
        )
    if "resourceMetadata" in data:
        import aws_sdk_inspector2.types.resource_scan_metadata

        out["resource_metadata"] = (
            aws_sdk_inspector2.types.resource_scan_metadata.deserialize_json(
                data["resourceMetadata"]
            )
        )
    if "lastScannedAt" in data:
        import aws_sdk_inspector2.types.date_time_timestamp

        out["last_scanned_at"] = (
            aws_sdk_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastScannedAt"]
            )
        )
    if "scanMode" in data:
        out["scan_mode"] = data["scanMode"]
    return out
