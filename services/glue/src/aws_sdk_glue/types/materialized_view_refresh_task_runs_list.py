"""Generated from Smithy shape ``com.amazonaws.glue#MaterializedViewRefreshTaskRunsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.materialized_view_refresh_task_run

MaterializedViewRefreshTaskRunsList: TypeAlias = list[
    "aws_sdk_glue.types.materialized_view_refresh_task_run.MaterializedViewRefreshTaskRun"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MaterializedViewRefreshTaskRunsList) -> list:
    import aws_sdk_glue.types.materialized_view_refresh_task_run

    out: list = []
    for item in value:
        out.append(
            aws_sdk_glue.types.materialized_view_refresh_task_run.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MaterializedViewRefreshTaskRunsList:
    import aws_sdk_glue.types.materialized_view_refresh_task_run

    out: MaterializedViewRefreshTaskRunsList = []
    for item in data:
        out.append(
            aws_sdk_glue.types.materialized_view_refresh_task_run.deserialize_aws_json_1_1(
                item
            )
        )
    return out
