"""Generated from Smithy shape ``com.amazonaws.glue#ColumnStatisticsTaskRunsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.column_statistics_task_run

ColumnStatisticsTaskRunsList: TypeAlias = list[
    "capo_glue.types.column_statistics_task_run.ColumnStatisticsTaskRun"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ColumnStatisticsTaskRunsList) -> list:
    import capo_glue.types.column_statistics_task_run

    out: list = []
    for item in value:
        out.append(
            capo_glue.types.column_statistics_task_run.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ColumnStatisticsTaskRunsList:
    import capo_glue.types.column_statistics_task_run

    out: ColumnStatisticsTaskRunsList = []
    for item in data:
        out.append(
            capo_glue.types.column_statistics_task_run.deserialize_aws_json_1_1(item)
        )
    return out
