"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanFindings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ecr.types.enhanced_image_scan_finding_list
    import aws_sdk_ecr.types.finding_severity_counts
    import aws_sdk_ecr.types.image_scan_finding_list
    import aws_sdk_ecr.types.scan_timestamp
    import aws_sdk_ecr.types.vulnerability_source_update_timestamp


class ImageScanFindings(TypedDict, closed=True):
    image_scan_completed_at: NotRequired[
        "aws_sdk_ecr.types.scan_timestamp.ScanTimestamp"
    ]
    """<p>The time of the last completed image scan.</p>"""
    vulnerability_source_updated_at: NotRequired[
        "aws_sdk_ecr.types.vulnerability_source_update_timestamp.VulnerabilitySourceUpdateTimestamp"
    ]
    """<p>The time when the vulnerability data was last scanned.</p>"""
    finding_severity_counts: NotRequired[
        "aws_sdk_ecr.types.finding_severity_counts.FindingSeverityCounts"
    ]
    """<p>The image vulnerability counts, sorted by severity.</p>"""
    findings: NotRequired[
        "aws_sdk_ecr.types.image_scan_finding_list.ImageScanFindingList"
    ]
    """<p>The findings from the image scan.</p>"""
    enhanced_findings: NotRequired[
        "aws_sdk_ecr.types.enhanced_image_scan_finding_list.EnhancedImageScanFindingList"
    ]
    """<p>Details about the enhanced scan findings from Amazon Inspector.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanFindings) -> dict:
    out: dict = {}
    if "image_scan_completed_at" in value:
        import aws_sdk_ecr.types.scan_timestamp

        out["imageScanCompletedAt"] = (
            aws_sdk_ecr.types.scan_timestamp.serialize_aws_json_1_1(
                value["image_scan_completed_at"]
            )
        )
    if "vulnerability_source_updated_at" in value:
        import aws_sdk_ecr.types.vulnerability_source_update_timestamp

        out["vulnerabilitySourceUpdatedAt"] = (
            aws_sdk_ecr.types.vulnerability_source_update_timestamp.serialize_aws_json_1_1(
                value["vulnerability_source_updated_at"]
            )
        )
    if "finding_severity_counts" in value:
        import aws_sdk_ecr.types.finding_severity_counts

        out["findingSeverityCounts"] = (
            aws_sdk_ecr.types.finding_severity_counts.serialize_aws_json_1_1(
                value["finding_severity_counts"]
            )
        )
    if "findings" in value:
        import aws_sdk_ecr.types.image_scan_finding_list

        out["findings"] = (
            aws_sdk_ecr.types.image_scan_finding_list.serialize_aws_json_1_1(
                value["findings"]
            )
        )
    if "enhanced_findings" in value:
        import aws_sdk_ecr.types.enhanced_image_scan_finding_list

        out["enhancedFindings"] = (
            aws_sdk_ecr.types.enhanced_image_scan_finding_list.serialize_aws_json_1_1(
                value["enhanced_findings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageScanFindings:
    out: ImageScanFindings = {}  # type: ignore[typeddict-item]
    if "imageScanCompletedAt" in data:
        import aws_sdk_ecr.types.scan_timestamp

        out["image_scan_completed_at"] = (
            aws_sdk_ecr.types.scan_timestamp.deserialize_aws_json_1_1(
                data["imageScanCompletedAt"]
            )
        )
    if "vulnerabilitySourceUpdatedAt" in data:
        import aws_sdk_ecr.types.vulnerability_source_update_timestamp

        out["vulnerability_source_updated_at"] = (
            aws_sdk_ecr.types.vulnerability_source_update_timestamp.deserialize_aws_json_1_1(
                data["vulnerabilitySourceUpdatedAt"]
            )
        )
    if "findingSeverityCounts" in data:
        import aws_sdk_ecr.types.finding_severity_counts

        out["finding_severity_counts"] = (
            aws_sdk_ecr.types.finding_severity_counts.deserialize_aws_json_1_1(
                data["findingSeverityCounts"]
            )
        )
    if "findings" in data:
        import aws_sdk_ecr.types.image_scan_finding_list

        out["findings"] = (
            aws_sdk_ecr.types.image_scan_finding_list.deserialize_aws_json_1_1(
                data["findings"]
            )
        )
    if "enhancedFindings" in data:
        import aws_sdk_ecr.types.enhanced_image_scan_finding_list

        out["enhanced_findings"] = (
            aws_sdk_ecr.types.enhanced_image_scan_finding_list.deserialize_aws_json_1_1(
                data["enhancedFindings"]
            )
        )
    return out
