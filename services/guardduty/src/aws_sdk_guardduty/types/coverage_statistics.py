"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.count_by_coverage_status
    import aws_sdk_guardduty.types.count_by_resource_type


class CoverageStatistics(TypedDict):
    count_by_resource_type: NotRequired[
        "aws_sdk_guardduty.types.count_by_resource_type.CountByResourceType"
    ]
    """<p>Represents coverage statistics for EKS clusters aggregated by resource type.</p>"""
    count_by_coverage_status: NotRequired[
        "aws_sdk_guardduty.types.count_by_coverage_status.CountByCoverageStatus"
    ]
    """<p>Represents coverage statistics for EKS clusters aggregated by coverage status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatistics) -> dict:
    out: dict = {}
    if "count_by_resource_type" in value:
        import aws_sdk_guardduty.types.count_by_resource_type

        out["countByResourceType"] = (
            aws_sdk_guardduty.types.count_by_resource_type.serialize_json(
                value["count_by_resource_type"]
            )
        )
    if "count_by_coverage_status" in value:
        import aws_sdk_guardduty.types.count_by_coverage_status

        out["countByCoverageStatus"] = (
            aws_sdk_guardduty.types.count_by_coverage_status.serialize_json(
                value["count_by_coverage_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageStatistics:
    out: CoverageStatistics = {}  # type: ignore[typeddict-item]
    if "countByResourceType" in data:
        import aws_sdk_guardduty.types.count_by_resource_type

        out["count_by_resource_type"] = (
            aws_sdk_guardduty.types.count_by_resource_type.deserialize_json(
                data["countByResourceType"]
            )
        )
    if "countByCoverageStatus" in data:
        import aws_sdk_guardduty.types.count_by_coverage_status

        out["count_by_coverage_status"] = (
            aws_sdk_guardduty.types.count_by_coverage_status.deserialize_json(
                data["countByCoverageStatus"]
            )
        )
    return out
