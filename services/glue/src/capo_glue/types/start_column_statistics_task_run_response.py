"""Generated from Smithy shape ``com.amazonaws.glue#StartColumnStatisticsTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.hash_string


class StartColumnStatisticsTaskRunResponse(TypedDict, closed=True):
    column_statistics_task_run_id: NotRequired["capo_glue.types.hash_string.HashString"]
    """<p>The identifier for the column statistics task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StartColumnStatisticsTaskRunResponse) -> dict:
    out: dict = {}
    if "column_statistics_task_run_id" in value:
        out["ColumnStatisticsTaskRunId"] = value["column_statistics_task_run_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StartColumnStatisticsTaskRunResponse:
    out: StartColumnStatisticsTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsTaskRunId" in data:
        out["column_statistics_task_run_id"] = data["ColumnStatisticsTaskRunId"]
    return out
