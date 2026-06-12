"""Generated from Smithy shape ``com.amazonaws.appstream#GetExportImageTaskRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appstream.types.uuid


class GetExportImageTaskRequest(TypedDict):
    task_id: NotRequired["aws_sdk_appstream.types.uuid.UUID"]
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
