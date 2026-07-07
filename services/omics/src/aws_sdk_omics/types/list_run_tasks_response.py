"""Generated from Smithy shape ``com.amazonaws.omics#ListRunTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_omics.types.task_list
    import aws_sdk_omics.types.task_list_token


class ListRunTasksResponse(TypedDict, closed=True):
    items: NotRequired["aws_sdk_omics.types.task_list.TaskList"]
    """<p>A list of tasks.</p>"""
    next_token: NotRequired["aws_sdk_omics.types.task_list_token.TaskListToken"]
    """<p>A pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRunTasksResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_omics.types.task_list

        out["items"] = aws_sdk_omics.types.task_list.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRunTasksResponse:
    out: ListRunTasksResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_omics.types.task_list

        out["items"] = aws_sdk_omics.types.task_list.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
