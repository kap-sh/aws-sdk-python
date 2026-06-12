"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics_task_runs_list
    import aws_sdk_glue.types.token


class GetColumnStatisticsTaskRunsResponse(TypedDict):
    column_statistics_task_runs: NotRequired[
        "aws_sdk_glue.types.column_statistics_task_runs_list.ColumnStatisticsTaskRunsList"
    ]
    """<p>A list of column statistics task runs.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if not all task runs have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskRunsResponse) -> dict:
    out: dict = {}
    if "column_statistics_task_runs" in value:
        import aws_sdk_glue.types.column_statistics_task_runs_list

        out["ColumnStatisticsTaskRuns"] = (
            aws_sdk_glue.types.column_statistics_task_runs_list.serialize_aws_json_1_1(
                value["column_statistics_task_runs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskRunsResponse:
    out: GetColumnStatisticsTaskRunsResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsTaskRuns" in data:
        import aws_sdk_glue.types.column_statistics_task_runs_list

        out["column_statistics_task_runs"] = (
            aws_sdk_glue.types.column_statistics_task_runs_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsTaskRuns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
