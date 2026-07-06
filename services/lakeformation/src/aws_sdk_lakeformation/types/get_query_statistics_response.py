"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetQueryStatisticsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.date_time
    import aws_sdk_lakeformation.types.execution_statistics
    import aws_sdk_lakeformation.types.planning_statistics


class GetQueryStatisticsResponse(TypedDict, closed=True):
    execution_statistics: NotRequired[
        "aws_sdk_lakeformation.types.execution_statistics.ExecutionStatistics"
    ]
    """<p>An <code>ExecutionStatistics</code> structure containing execution statistics.</p>"""
    planning_statistics: NotRequired[
        "aws_sdk_lakeformation.types.planning_statistics.PlanningStatistics"
    ]
    """<p>A <code>PlanningStatistics</code> structure containing query planning statistics.</p>"""
    query_submission_time: NotRequired["aws_sdk_lakeformation.types.date_time.DateTime"]
    """<p>The time that the query was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQueryStatisticsResponse) -> dict:
    out: dict = {}
    if "execution_statistics" in value:
        import aws_sdk_lakeformation.types.execution_statistics

        out["ExecutionStatistics"] = (
            aws_sdk_lakeformation.types.execution_statistics.serialize_json(
                value["execution_statistics"]
            )
        )
    if "planning_statistics" in value:
        import aws_sdk_lakeformation.types.planning_statistics

        out["PlanningStatistics"] = (
            aws_sdk_lakeformation.types.planning_statistics.serialize_json(
                value["planning_statistics"]
            )
        )
    if "query_submission_time" in value:
        import aws_sdk_lakeformation.types.date_time

        out["QuerySubmissionTime"] = (
            aws_sdk_lakeformation.types.date_time.serialize_json(
                value["query_submission_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetQueryStatisticsResponse:
    out: GetQueryStatisticsResponse = {}  # type: ignore[typeddict-item]
    if "ExecutionStatistics" in data:
        import aws_sdk_lakeformation.types.execution_statistics

        out["execution_statistics"] = (
            aws_sdk_lakeformation.types.execution_statistics.deserialize_json(
                data["ExecutionStatistics"]
            )
        )
    if "PlanningStatistics" in data:
        import aws_sdk_lakeformation.types.planning_statistics

        out["planning_statistics"] = (
            aws_sdk_lakeformation.types.planning_statistics.deserialize_json(
                data["PlanningStatistics"]
            )
        )
    if "QuerySubmissionTime" in data:
        import aws_sdk_lakeformation.types.date_time

        out["query_submission_time"] = (
            aws_sdk_lakeformation.types.date_time.deserialize_json(
                data["QuerySubmissionTime"]
            )
        )
    return out
