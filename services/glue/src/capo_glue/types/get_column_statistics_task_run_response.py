"""Generated from Smithy shape ``com.amazonaws.glue#GetColumnStatisticsTaskRunResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.column_statistics_task_run


class GetColumnStatisticsTaskRunResponse(TypedDict, closed=True):
    column_statistics_task_run: NotRequired[
        "capo_glue.types.column_statistics_task_run.ColumnStatisticsTaskRun"
    ]
    """<p>A <code>ColumnStatisticsTaskRun</code> object representing the details of the column stats run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetColumnStatisticsTaskRunResponse) -> dict:
    out: dict = {}
    if "column_statistics_task_run" in value:
        import capo_glue.types.column_statistics_task_run

        out["ColumnStatisticsTaskRun"] = (
            capo_glue.types.column_statistics_task_run.serialize_aws_json_1_1(
                value["column_statistics_task_run"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetColumnStatisticsTaskRunResponse:
    out: GetColumnStatisticsTaskRunResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsTaskRun" in data:
        import capo_glue.types.column_statistics_task_run

        out["column_statistics_task_run"] = (
            capo_glue.types.column_statistics_task_run.deserialize_aws_json_1_1(
                data["ColumnStatisticsTaskRun"]
            )
        )
    return out
