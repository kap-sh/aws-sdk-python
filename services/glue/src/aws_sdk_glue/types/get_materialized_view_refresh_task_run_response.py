"""Generated from Smithy shape ``com.amazonaws.glue#GetMaterializedViewRefreshTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.materialized_view_refresh_task_run


class GetMaterializedViewRefreshTaskRunResponse(TypedDict, closed=True):
    materialized_view_refresh_task_run: NotRequired[
        "aws_sdk_glue.types.materialized_view_refresh_task_run.MaterializedViewRefreshTaskRun"
    ]
    """<p>A MaterializedViewRefreshTaskRun object representing the details of the task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMaterializedViewRefreshTaskRunResponse) -> dict:
    out: dict = {}
    if "materialized_view_refresh_task_run" in value:
        import aws_sdk_glue.types.materialized_view_refresh_task_run

        out["MaterializedViewRefreshTaskRun"] = (
            aws_sdk_glue.types.materialized_view_refresh_task_run.serialize_aws_json_1_1(
                value["materialized_view_refresh_task_run"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMaterializedViewRefreshTaskRunResponse:
    out: GetMaterializedViewRefreshTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "MaterializedViewRefreshTaskRun" in data:
        import aws_sdk_glue.types.materialized_view_refresh_task_run

        out["materialized_view_refresh_task_run"] = (
            aws_sdk_glue.types.materialized_view_refresh_task_run.deserialize_aws_json_1_1(
                data["MaterializedViewRefreshTaskRun"]
            )
        )
    return out
