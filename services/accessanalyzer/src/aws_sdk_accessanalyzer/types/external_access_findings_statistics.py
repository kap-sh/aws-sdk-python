"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ExternalAccessFindingsStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.resource_type_statistics_map


class ExternalAccessFindingsStatistics(TypedDict, closed=True):
    resource_type_statistics: NotRequired[
        "aws_sdk_accessanalyzer.types.resource_type_statistics_map.ResourceTypeStatisticsMap"
    ]
    """<p>The total number of active cross-account and public findings for each resource type of the specified external access analyzer.</p>"""
    total_active_findings: NotRequired["int"]
    """<p>The number of active findings for the specified external access analyzer.</p>"""
    total_archived_findings: NotRequired["int"]
    """<p>The number of archived findings for the specified external access analyzer.</p>"""
    total_resolved_findings: NotRequired["int"]
    """<p>The number of resolved findings for the specified external access analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExternalAccessFindingsStatistics) -> dict:
    out: dict = {}
    if "resource_type_statistics" in value:
        import aws_sdk_accessanalyzer.types.resource_type_statistics_map

        out["resourceTypeStatistics"] = (
            aws_sdk_accessanalyzer.types.resource_type_statistics_map.serialize_json(
                value["resource_type_statistics"]
            )
        )
    if "total_active_findings" in value:
        out["totalActiveFindings"] = value["total_active_findings"]
    if "total_archived_findings" in value:
        out["totalArchivedFindings"] = value["total_archived_findings"]
    if "total_resolved_findings" in value:
        out["totalResolvedFindings"] = value["total_resolved_findings"]
    return out


def deserialize_json(data: dict) -> ExternalAccessFindingsStatistics:
    out: ExternalAccessFindingsStatistics = {}  # type: ignore[typeddict-item]
    if "resourceTypeStatistics" in data:
        import aws_sdk_accessanalyzer.types.resource_type_statistics_map

        out["resource_type_statistics"] = (
            aws_sdk_accessanalyzer.types.resource_type_statistics_map.deserialize_json(
                data["resourceTypeStatistics"]
            )
        )
    if "totalActiveFindings" in data:
        out["total_active_findings"] = data["totalActiveFindings"]
    if "totalArchivedFindings" in data:
        out["total_archived_findings"] = data["totalArchivedFindings"]
    if "totalResolvedFindings" in data:
        out["total_resolved_findings"] = data["totalResolvedFindings"]
    return out
