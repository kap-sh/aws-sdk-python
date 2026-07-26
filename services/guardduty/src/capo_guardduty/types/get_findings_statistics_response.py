"""Generated from Smithy shape ``com.amazonaws.guardduty#GetFindingsStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.finding_statistics
    import capo_guardduty.types.string


class GetFindingsStatisticsResponse(TypedDict, closed=True):
    finding_statistics: NotRequired[
        "capo_guardduty.types.finding_statistics.FindingStatistics"
    ]
    """<p>The finding statistics object.</p>"""
    next_token: NotRequired["capo_guardduty.types.string.String"]
    """<p>The pagination parameter to be used on the next list operation to retrieve more items.</p> <p>This parameter is currently not supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFindingsStatisticsResponse) -> dict:
    out: dict = {}
    if "finding_statistics" in value:
        import capo_guardduty.types.finding_statistics

        out["findingStatistics"] = (
            capo_guardduty.types.finding_statistics.serialize_json(
                value["finding_statistics"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetFindingsStatisticsResponse:
    out: GetFindingsStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "findingStatistics" in data:
        import capo_guardduty.types.finding_statistics

        out["finding_statistics"] = (
            capo_guardduty.types.finding_statistics.deserialize_json(
                data["findingStatistics"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
