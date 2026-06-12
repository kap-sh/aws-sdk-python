"""Generated from Smithy shape ``com.amazonaws.glue#ListMaterializedViewRefreshTaskRunsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.materialized_view_refresh_task_runs_list
    import aws_sdk_glue.types.token


class ListMaterializedViewRefreshTaskRunsResponse(TypedDict):
    materialized_view_refresh_task_runs: NotRequired[
        "aws_sdk_glue.types.materialized_view_refresh_task_runs_list.MaterializedViewRefreshTaskRunsList"
    ]
    """<p>The results of the ListMaterializedViewRefreshTaskRuns action. </p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if not all task run IDs have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListMaterializedViewRefreshTaskRunsResponse) -> dict:
    out: dict = {}
    if "materialized_view_refresh_task_runs" in value:
        import aws_sdk_glue.types.materialized_view_refresh_task_runs_list

        out["MaterializedViewRefreshTaskRuns"] = (
            aws_sdk_glue.types.materialized_view_refresh_task_runs_list.serialize_aws_json_1_1(
                value["materialized_view_refresh_task_runs"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListMaterializedViewRefreshTaskRunsResponse:
    out: ListMaterializedViewRefreshTaskRunsResponse = {}  # type: ignore[typeddict-item]
    if "MaterializedViewRefreshTaskRuns" in data:
        import aws_sdk_glue.types.materialized_view_refresh_task_runs_list

        out["materialized_view_refresh_task_runs"] = (
            aws_sdk_glue.types.materialized_view_refresh_task_runs_list.deserialize_aws_json_1_1(
                data["MaterializedViewRefreshTaskRuns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
