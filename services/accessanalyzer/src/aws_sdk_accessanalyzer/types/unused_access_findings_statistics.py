"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#UnusedAccessFindingsStatistics``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.account_aggregations
    import aws_sdk_accessanalyzer.types.unused_access_type_statistics_list


class UnusedAccessFindingsStatistics(TypedDict):
    unused_access_type_statistics: NotRequired[
        "aws_sdk_accessanalyzer.types.unused_access_type_statistics_list.UnusedAccessTypeStatisticsList"
    ]
    """<p>A list of details about the total number of findings for each type of unused access for the analyzer. </p>"""
    top_accounts: NotRequired[
        "aws_sdk_accessanalyzer.types.account_aggregations.AccountAggregations"
    ]
    """<p>A list of one to ten Amazon Web Services accounts that have the most active findings for the unused access analyzer.</p>"""
    total_active_findings: NotRequired["int"]
    """<p>The total number of active findings for the unused access analyzer.</p>"""
    total_archived_findings: NotRequired["int"]
    """<p>The total number of archived findings for the unused access analyzer.</p>"""
    total_resolved_findings: NotRequired["int"]
    """<p>The total number of resolved findings for the unused access analyzer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnusedAccessFindingsStatistics) -> dict:
    out: dict = {}
    if "unused_access_type_statistics" in value:
        import aws_sdk_accessanalyzer.types.unused_access_type_statistics_list

        out["unusedAccessTypeStatistics"] = (
            aws_sdk_accessanalyzer.types.unused_access_type_statistics_list.serialize_json(
                value["unused_access_type_statistics"]
            )
        )
    if "top_accounts" in value:
        import aws_sdk_accessanalyzer.types.account_aggregations

        out["topAccounts"] = (
            aws_sdk_accessanalyzer.types.account_aggregations.serialize_json(
                value["top_accounts"]
            )
        )
    if "total_active_findings" in value:
        out["totalActiveFindings"] = value["total_active_findings"]
    if "total_archived_findings" in value:
        out["totalArchivedFindings"] = value["total_archived_findings"]
    if "total_resolved_findings" in value:
        out["totalResolvedFindings"] = value["total_resolved_findings"]
    return out


def deserialize_json(data: dict) -> UnusedAccessFindingsStatistics:
    out: UnusedAccessFindingsStatistics = {}  # type: ignore[typeddict-item]
    if "unusedAccessTypeStatistics" in data:
        import aws_sdk_accessanalyzer.types.unused_access_type_statistics_list

        out["unused_access_type_statistics"] = (
            aws_sdk_accessanalyzer.types.unused_access_type_statistics_list.deserialize_json(
                data["unusedAccessTypeStatistics"]
            )
        )
    if "topAccounts" in data:
        import aws_sdk_accessanalyzer.types.account_aggregations

        out["top_accounts"] = (
            aws_sdk_accessanalyzer.types.account_aggregations.deserialize_json(
                data["topAccounts"]
            )
        )
    if "totalActiveFindings" in data:
        out["total_active_findings"] = data["totalActiveFindings"]
    if "totalArchivedFindings" in data:
        out["total_archived_findings"] = data["totalArchivedFindings"]
    if "totalResolvedFindings" in data:
        out["total_resolved_findings"] = data["totalResolvedFindings"]
    return out
