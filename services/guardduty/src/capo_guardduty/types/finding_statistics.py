"""Generated from Smithy shape ``com.amazonaws.guardduty#FindingStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.count_by_severity
    import capo_guardduty.types.grouped_by_account
    import capo_guardduty.types.grouped_by_date
    import capo_guardduty.types.grouped_by_finding_type
    import capo_guardduty.types.grouped_by_resource
    import capo_guardduty.types.grouped_by_severity


class FindingStatistics(TypedDict, closed=True):
    count_by_severity: NotRequired[
        "capo_guardduty.types.count_by_severity.CountBySeverity"
    ]
    """<p>Represents a list of map of severity to count statistics for a set of findings.</p>"""
    grouped_by_account: NotRequired[
        "capo_guardduty.types.grouped_by_account.GroupedByAccount"
    ]
    """<p>Represents a list of map of accounts with a findings count associated with each account.</p>"""
    grouped_by_date: NotRequired["capo_guardduty.types.grouped_by_date.GroupedByDate"]
    """<p>Represents a list of map of dates with a count of total findings generated on each date per severity level.</p>"""
    grouped_by_finding_type: NotRequired[
        "capo_guardduty.types.grouped_by_finding_type.GroupedByFindingType"
    ]
    """<p>Represents a list of map of finding types with a count of total findings generated for each type. </p> <p>Based on the <code>orderBy</code> parameter, this request returns either the most occurring finding types or the least occurring finding types. If the <code>orderBy</code> parameter is <code>ASC</code>, this will represent the least occurring finding types in your account; otherwise, this will represent the most occurring finding types. The default value of <code>orderBy</code> is <code>DESC</code>.</p>"""
    grouped_by_resource: NotRequired[
        "capo_guardduty.types.grouped_by_resource.GroupedByResource"
    ]
    """<p>Represents a list of map of top resources with a count of total findings.</p>"""
    grouped_by_severity: NotRequired[
        "capo_guardduty.types.grouped_by_severity.GroupedBySeverity"
    ]
    """<p>Represents a list of map of total findings for each severity level.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatistics) -> dict:
    out: dict = {}
    if "count_by_severity" in value:
        import capo_guardduty.types.count_by_severity

        out["countBySeverity"] = capo_guardduty.types.count_by_severity.serialize_json(
            value["count_by_severity"]
        )
    if "grouped_by_account" in value:
        import capo_guardduty.types.grouped_by_account

        out["groupedByAccount"] = (
            capo_guardduty.types.grouped_by_account.serialize_json(
                value["grouped_by_account"]
            )
        )
    if "grouped_by_date" in value:
        import capo_guardduty.types.grouped_by_date

        out["groupedByDate"] = capo_guardduty.types.grouped_by_date.serialize_json(
            value["grouped_by_date"]
        )
    if "grouped_by_finding_type" in value:
        import capo_guardduty.types.grouped_by_finding_type

        out["groupedByFindingType"] = (
            capo_guardduty.types.grouped_by_finding_type.serialize_json(
                value["grouped_by_finding_type"]
            )
        )
    if "grouped_by_resource" in value:
        import capo_guardduty.types.grouped_by_resource

        out["groupedByResource"] = (
            capo_guardduty.types.grouped_by_resource.serialize_json(
                value["grouped_by_resource"]
            )
        )
    if "grouped_by_severity" in value:
        import capo_guardduty.types.grouped_by_severity

        out["groupedBySeverity"] = (
            capo_guardduty.types.grouped_by_severity.serialize_json(
                value["grouped_by_severity"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingStatistics:
    out: FindingStatistics = {}  # type: ignore[typeddict-item]
    if "countBySeverity" in data:
        import capo_guardduty.types.count_by_severity

        out["count_by_severity"] = (
            capo_guardduty.types.count_by_severity.deserialize_json(
                data["countBySeverity"]
            )
        )
    if "groupedByAccount" in data:
        import capo_guardduty.types.grouped_by_account

        out["grouped_by_account"] = (
            capo_guardduty.types.grouped_by_account.deserialize_json(
                data["groupedByAccount"]
            )
        )
    if "groupedByDate" in data:
        import capo_guardduty.types.grouped_by_date

        out["grouped_by_date"] = capo_guardduty.types.grouped_by_date.deserialize_json(
            data["groupedByDate"]
        )
    if "groupedByFindingType" in data:
        import capo_guardduty.types.grouped_by_finding_type

        out["grouped_by_finding_type"] = (
            capo_guardduty.types.grouped_by_finding_type.deserialize_json(
                data["groupedByFindingType"]
            )
        )
    if "groupedByResource" in data:
        import capo_guardduty.types.grouped_by_resource

        out["grouped_by_resource"] = (
            capo_guardduty.types.grouped_by_resource.deserialize_json(
                data["groupedByResource"]
            )
        )
    if "groupedBySeverity" in data:
        import capo_guardduty.types.grouped_by_severity

        out["grouped_by_severity"] = (
            capo_guardduty.types.grouped_by_severity.deserialize_json(
                data["groupedBySeverity"]
            )
        )
    return out
