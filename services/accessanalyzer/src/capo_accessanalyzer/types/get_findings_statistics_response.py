"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#GetFindingsStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_accessanalyzer.types.findings_statistics_list
    import capo_accessanalyzer.types.timestamp


class GetFindingsStatisticsResponse(TypedDict, closed=True):
    findings_statistics: NotRequired[
        "capo_accessanalyzer.types.findings_statistics_list.FindingsStatisticsList"
    ]
    """<p>A group of external access or unused access findings statistics.</p>"""
    last_updated_at: NotRequired["capo_accessanalyzer.types.timestamp.Timestamp"]
    """<p>The time at which the retrieval of the findings statistics was last updated. If the findings statistics have not been previously retrieved for the specified analyzer, this field will not be populated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsStatisticsResponse) -> dict:
    out: dict = {}
    if "findings_statistics" in value:
        import capo_accessanalyzer.types.findings_statistics_list

        out["findingsStatistics"] = (
            capo_accessanalyzer.types.findings_statistics_list.serialize_json(
                value["findings_statistics"]
            )
        )
    if "last_updated_at" in value:
        import capo_accessanalyzer.types.timestamp

        out["lastUpdatedAt"] = capo_accessanalyzer.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    return out


def deserialize_json(data: dict) -> GetFindingsStatisticsResponse:
    out: GetFindingsStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "findingsStatistics" in data:
        import capo_accessanalyzer.types.findings_statistics_list

        out["findings_statistics"] = (
            capo_accessanalyzer.types.findings_statistics_list.deserialize_json(
                data["findingsStatistics"]
            )
        )
    if "lastUpdatedAt" in data:
        import capo_accessanalyzer.types.timestamp

        out["last_updated_at"] = capo_accessanalyzer.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    return out
