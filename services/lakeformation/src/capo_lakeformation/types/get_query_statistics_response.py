"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetQueryStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.date_time
    import capo_lakeformation.types.execution_statistics
    import capo_lakeformation.types.planning_statistics


class GetQueryStatisticsResponse(TypedDict, closed=True):
    execution_statistics: NotRequired[
        "capo_lakeformation.types.execution_statistics.ExecutionStatistics"
    ]
    """<p>An <code>ExecutionStatistics</code> structure containing execution statistics.</p>"""
    planning_statistics: NotRequired[
        "capo_lakeformation.types.planning_statistics.PlanningStatistics"
    ]
    """<p>A <code>PlanningStatistics</code> structure containing query planning statistics.</p>"""
    query_submission_time: NotRequired["capo_lakeformation.types.date_time.DateTime"]
    """<p>The time that the query was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatisticsResponse) -> dict:
    out: dict = {}
    if "execution_statistics" in value:
        import capo_lakeformation.types.execution_statistics

        out["ExecutionStatistics"] = (
            capo_lakeformation.types.execution_statistics.serialize_json(
                value["execution_statistics"]
            )
        )
    if "planning_statistics" in value:
        import capo_lakeformation.types.planning_statistics

        out["PlanningStatistics"] = (
            capo_lakeformation.types.planning_statistics.serialize_json(
                value["planning_statistics"]
            )
        )
    if "query_submission_time" in value:
        import capo_lakeformation.types.date_time

        out["QuerySubmissionTime"] = capo_lakeformation.types.date_time.serialize_json(
            value["query_submission_time"]
        )
    return out


def deserialize_json(data: dict) -> GetQueryStatisticsResponse:
    out: GetQueryStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionStatistics" in data:
        import capo_lakeformation.types.execution_statistics

        out["execution_statistics"] = (
            capo_lakeformation.types.execution_statistics.deserialize_json(
                data["ExecutionStatistics"]
            )
        )
    if "PlanningStatistics" in data:
        import capo_lakeformation.types.planning_statistics

        out["planning_statistics"] = (
            capo_lakeformation.types.planning_statistics.deserialize_json(
                data["PlanningStatistics"]
            )
        )
    if "QuerySubmissionTime" in data:
        import capo_lakeformation.types.date_time

        out["query_submission_time"] = (
            capo_lakeformation.types.date_time.deserialize_json(
                data["QuerySubmissionTime"]
            )
        )
    return out
