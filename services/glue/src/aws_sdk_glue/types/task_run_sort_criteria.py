"""Generated from Smithy shape ``com.amazonaws.glue#TaskRunSortCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_glue.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_glue.types.sort_direction_type
    import aws_sdk_glue.types.task_run_sort_column_type


class TaskRunSortCriteria(TypedDict):
    column: "aws_sdk_glue.types.task_run_sort_column_type.TaskRunSortColumnType"
    """<p>The column to be used to sort the list of task runs for the machine learning transform.</p>"""
    sort_direction: "aws_sdk_glue.types.sort_direction_type.SortDirectionType"
    """<p>The sort direction to be used to sort the list of task runs for the machine learning transform.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskRunSortCriteria) -> dict:
    out: dict = {}
    import aws_sdk_glue.types.task_run_sort_column_type

    out["Column"] = aws_sdk_glue.types.task_run_sort_column_type.serialize_aws_json_1_1(
        value["column"]
    )
    import aws_sdk_glue.types.sort_direction_type

    out["SortDirection"] = (
        aws_sdk_glue.types.sort_direction_type.serialize_aws_json_1_1(
            value["sort_direction"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskRunSortCriteria:
    out: TaskRunSortCriteria = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_glue.types.task_run_sort_column_type

        out["column"] = (
            aws_sdk_glue.types.task_run_sort_column_type.deserialize_aws_json_1_1(
                data["Column"]
            )
        )
    else:
        raise DeserializationError("TaskRunSortCriteria.column required")
    if "SortDirection" in data:
        import aws_sdk_glue.types.sort_direction_type

        out["sort_direction"] = (
            aws_sdk_glue.types.sort_direction_type.deserialize_aws_json_1_1(
                data["SortDirection"]
            )
        )
    else:
        raise DeserializationError("TaskRunSortCriteria.sort_direction required")
    return out
