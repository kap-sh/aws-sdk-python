"""Generated from Smithy shape ``com.amazonaws.glue#ListColumnStatisticsTaskRunsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.column_statistics_task_run_id_list
    import aws_sdk_glue.types.token


class ListColumnStatisticsTaskRunsResponse(TypedDict, closed=True):
    column_statistics_task_run_ids: NotRequired[
        "aws_sdk_glue.types.column_statistics_task_run_id_list.ColumnStatisticsTaskRunIdList"
    ]
    """<p>A list of column statistics task run IDs.</p>"""
    next_token: NotRequired["aws_sdk_glue.types.token.Token"]
    """<p>A continuation token, if not all task run IDs have yet been returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListColumnStatisticsTaskRunsResponse) -> dict:
    out: dict = {}
    if "column_statistics_task_run_ids" in value:
        import aws_sdk_glue.types.column_statistics_task_run_id_list

        out["ColumnStatisticsTaskRunIds"] = (
            aws_sdk_glue.types.column_statistics_task_run_id_list.serialize_aws_json_1_1(
                value["column_statistics_task_run_ids"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListColumnStatisticsTaskRunsResponse:
    out: ListColumnStatisticsTaskRunsResponse = {}  # type: ignore[typeddict-item]
    if "ColumnStatisticsTaskRunIds" in data:
        import aws_sdk_glue.types.column_statistics_task_run_id_list

        out["column_statistics_task_run_ids"] = (
            aws_sdk_glue.types.column_statistics_task_run_id_list.deserialize_aws_json_1_1(
                data["ColumnStatisticsTaskRunIds"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
