"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetImportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.data_set_import_summary
    import capo_m2.types.data_set_task_lifecycle
    import capo_m2.types.identifier


class GetDataSetImportTaskResponse(TypedDict, closed=True):
    task_id: "capo_m2.types.identifier.Identifier"
    """<p>The task identifier.</p>"""
    status: "capo_m2.types.data_set_task_lifecycle.DataSetTaskLifecycle"
    """<p>The status of the task.</p>"""
    summary: NotRequired["capo_m2.types.data_set_import_summary.DataSetImportSummary"]
    """<p>A summary of the status of the task.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetImportTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    out["status"] = value["status"]
    if "summary" in value:
        import capo_m2.types.data_set_import_summary

        out["summary"] = capo_m2.types.data_set_import_summary.serialize_json(
            value["summary"]
        )
    return out


def deserialize_json(data: dict) -> GetDataSetImportTaskResponse:
    out: GetDataSetImportTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("GetDataSetImportTaskResponse.task_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetDataSetImportTaskResponse.status required")
    if "summary" in data:
        import capo_m2.types.data_set_import_summary

        out["summary"] = capo_m2.types.data_set_import_summary.deserialize_json(
            data["summary"]
        )
    return out
