"""Generated from Smithy shape ``com.amazonaws.guardduty#CoverageStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count_by_coverage_status
    import capo_guardduty.types.count_by_resource_type


class CoverageStatistics(TypedDict, closed=True):
    count_by_resource_type: NotRequired[
        "capo_guardduty.types.count_by_resource_type.CountByResourceType"
    ]
    """<p>Represents coverage statistics for EKS clusters aggregated by resource type.</p>"""
    count_by_coverage_status: NotRequired[
        "capo_guardduty.types.count_by_coverage_status.CountByCoverageStatus"
    ]
    """<p>Represents coverage statistics for EKS clusters aggregated by coverage status.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoverageStatistics) -> dict:
    out: dict = {}
    if "count_by_resource_type" in value:
        import capo_guardduty.types.count_by_resource_type

        out["countByResourceType"] = (
            capo_guardduty.types.count_by_resource_type.serialize_json(
                value["count_by_resource_type"]
            )
        )
    if "count_by_coverage_status" in value:
        import capo_guardduty.types.count_by_coverage_status

        out["countByCoverageStatus"] = (
            capo_guardduty.types.count_by_coverage_status.serialize_json(
                value["count_by_coverage_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoverageStatistics:
    out: CoverageStatistics = {}  # type: ignore[typeddict-item]
    if "countByResourceType" in data:
        import capo_guardduty.types.count_by_resource_type

        out["count_by_resource_type"] = (
            capo_guardduty.types.count_by_resource_type.deserialize_json(
                data["countByResourceType"]
            )
        )
    if "countByCoverageStatus" in data:
        import capo_guardduty.types.count_by_coverage_status

        out["count_by_coverage_status"] = (
            capo_guardduty.types.count_by_coverage_status.deserialize_json(
                data["countByCoverageStatus"]
            )
        )
    return out
