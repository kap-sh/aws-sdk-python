"""Generated from Smithy shape ``com.amazonaws.glue#StartMaterializedViewRefreshTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.uui_dv4


class StartMaterializedViewRefreshTaskRunResponse(TypedDict, closed=True):
    materialized_view_refresh_task_run_id: NotRequired["capo_glue.types.uui_dv4.UUIDv4"]
    """<p>The identifier for the materialized view refresh task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartMaterializedViewRefreshTaskRunResponse) -> dict:
    out: dict = {}
    if "materialized_view_refresh_task_run_id" in value:
        out["MaterializedViewRefreshTaskRunId"] = value[
            "materialized_view_refresh_task_run_id"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartMaterializedViewRefreshTaskRunResponse:
    out: StartMaterializedViewRefreshTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "MaterializedViewRefreshTaskRunId" in data:
        out["materialized_view_refresh_task_run_id"] = data[
            "MaterializedViewRefreshTaskRunId"
        ]
    return out
