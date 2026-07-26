"""Generated from Smithy shape ``com.amazonaws.appstream#GetExportImageTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.uuid


class GetExportImageTaskRequest(TypedDict, closed=True):
    task_id: NotRequired["capo_appstream.types.uuid.UUID"]
    """<p>The unique identifier of the export image task to retrieve information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetExportImageTaskRequest) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["TaskId"] = value["task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetExportImageTaskRequest:
    out: GetExportImageTaskRequest = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    return out
