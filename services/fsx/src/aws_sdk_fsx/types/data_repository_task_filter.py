"""Generated from Smithy shape ``com.amazonaws.fsx#DataRepositoryTaskFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fsx.types.data_repository_task_filter_name
    import aws_sdk_fsx.types.data_repository_task_filter_values


class DataRepositoryTaskFilter(TypedDict, closed=True):
    name: NotRequired[
        "aws_sdk_fsx.types.data_repository_task_filter_name.DataRepositoryTaskFilterName"
    ]
    """<p>Name of the task property to use in filtering the tasks returned in the response.</p> <ul> <li> <p>Use <code>file-system-id</code> to retrieve data repository tasks for specific file systems.</p> </li> <li> <p>Use <code>task-lifecycle</code> to retrieve data repository tasks with one or more specific lifecycle states, as follows: CANCELED, EXECUTING, FAILED, PENDING, and SUCCEEDED.</p> </li> </ul>"""
    values: NotRequired[
        "aws_sdk_fsx.types.data_repository_task_filter_values.DataRepositoryTaskFilterValues"
    ]
    """<p>Use Values to include the specific file system IDs and task lifecycle states for the filters you are using.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataRepositoryTaskFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import aws_sdk_fsx.types.data_repository_task_filter_name

        out["Name"] = (
            aws_sdk_fsx.types.data_repository_task_filter_name.serialize_aws_json_1_1(
                value["name"]
            )
        )
    if "values" in value:
        import aws_sdk_fsx.types.data_repository_task_filter_values

        out["Values"] = (
            aws_sdk_fsx.types.data_repository_task_filter_values.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataRepositoryTaskFilter:
    out: DataRepositoryTaskFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_fsx.types.data_repository_task_filter_name

        out["name"] = (
            aws_sdk_fsx.types.data_repository_task_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    if "Values" in data:
        import aws_sdk_fsx.types.data_repository_task_filter_values

        out["values"] = (
            aws_sdk_fsx.types.data_repository_task_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
