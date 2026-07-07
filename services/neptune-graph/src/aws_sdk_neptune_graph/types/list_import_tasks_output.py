"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ListImportTasksOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune_graph.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.import_task_summary_list
    import aws_sdk_neptune_graph.types.pagination_token


class ListImportTasksOutput(TypedDict, closed=True):
    tasks: "aws_sdk_neptune_graph.types.import_task_summary_list.ImportTaskSummaryList"
    """<p>The requested list of import tasks.</p>"""
    next_token: NotRequired[
        "aws_sdk_neptune_graph.types.pagination_token.PaginationToken"
    ]
    """<p>Pagination token used to paginate output.</p> <p>When this value is provided as input, the service returns results from where the previous response left off. When this value is present in output, it indicates that there are more results to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportTasksOutput) -> dict:
    out: dict = {}
    import aws_sdk_neptune_graph.types.import_task_summary_list

    out["tasks"] = aws_sdk_neptune_graph.types.import_task_summary_list.serialize_json(
        value["tasks"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportTasksOutput:
    out: ListImportTasksOutput = {}  # type: ignore[typeddict-item]
    if "tasks" in data:
        import aws_sdk_neptune_graph.types.import_task_summary_list

        out["tasks"] = (
            aws_sdk_neptune_graph.types.import_task_summary_list.deserialize_json(
                data["tasks"]
            )
        )
    else:
        raise DeserializationError("ListImportTasksOutput.tasks required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
