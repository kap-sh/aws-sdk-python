"""Generated from Smithy shape ``com.amazonaws.ecr#ImageScanFindingsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.finding_severity_counts
    import capo_ecr.types.scan_timestamp
    import capo_ecr.types.vulnerability_source_update_timestamp


class ImageScanFindingsSummary(TypedDict, closed=True):
    image_scan_completed_at: NotRequired["capo_ecr.types.scan_timestamp.ScanTimestamp"]
    """<p>The time of the last completed image scan.</p>"""
    vulnerability_source_updated_at: NotRequired[
        "capo_ecr.types.vulnerability_source_update_timestamp.VulnerabilitySourceUpdateTimestamp"
    ]
    """<p>The time when the vulnerability data was last scanned.</p>"""
    finding_severity_counts: NotRequired[
        "capo_ecr.types.finding_severity_counts.FindingSeverityCounts"
    ]
    """<p>The image vulnerability counts, sorted by severity.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageScanFindingsSummary) -> dict:
    out: dict = {}
    if "image_scan_completed_at" in value:
        import capo_ecr.types.scan_timestamp

        out["imageScanCompletedAt"] = (
            capo_ecr.types.scan_timestamp.serialize_aws_json_1_1(
                value["image_scan_completed_at"]
            )
        )
    if "vulnerability_source_updated_at" in value:
        import capo_ecr.types.vulnerability_source_update_timestamp

        out["vulnerabilitySourceUpdatedAt"] = (
            capo_ecr.types.vulnerability_source_update_timestamp.serialize_aws_json_1_1(
                value["vulnerability_source_updated_at"]
            )
        )
    if "finding_severity_counts" in value:
        import capo_ecr.types.finding_severity_counts

        out["findingSeverityCounts"] = (
            capo_ecr.types.finding_severity_counts.serialize_aws_json_1_1(
                value["finding_severity_counts"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImageScanFindingsSummary:
    out: ImageScanFindingsSummary = {}  # type: ignore[typeddict-item]
    if "imageScanCompletedAt" in data:
        import capo_ecr.types.scan_timestamp

        out["image_scan_completed_at"] = (
            capo_ecr.types.scan_timestamp.deserialize_aws_json_1_1(
                data["imageScanCompletedAt"]
            )
        )
    if "vulnerabilitySourceUpdatedAt" in data:
        import capo_ecr.types.vulnerability_source_update_timestamp

        out["vulnerability_source_updated_at"] = (
            capo_ecr.types.vulnerability_source_update_timestamp.deserialize_aws_json_1_1(
                data["vulnerabilitySourceUpdatedAt"]
            )
        )
    if "findingSeverityCounts" in data:
        import capo_ecr.types.finding_severity_counts

        out["finding_severity_counts"] = (
            capo_ecr.types.finding_severity_counts.deserialize_aws_json_1_1(
                data["findingSeverityCounts"]
            )
        )
    return out
