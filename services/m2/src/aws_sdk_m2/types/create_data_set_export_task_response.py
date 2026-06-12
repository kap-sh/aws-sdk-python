"""Generated from Smithy shape ``com.amazonaws.m2#CreateDataSetExportTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.identifier


class CreateDataSetExportTaskResponse(TypedDict):
    task_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The task identifier. This operation is asynchronous. Use this identifier with the <a>GetDataSetExportTask</a> operation to obtain the status of this task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataSetExportTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> CreateDataSetExportTaskResponse:
    out: CreateDataSetExportTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("CreateDataSetExportTaskResponse.task_id required")
    return out
