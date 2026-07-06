"""Generated from Smithy shape ``com.amazonaws.m2#DataSetImportTask``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_import_summary
    import aws_sdk_m2.types.data_set_task_lifecycle
    import aws_sdk_m2.types.identifier


class DataSetImportTask(TypedDict, closed=True):
    task_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The identifier of the data set import task.</p>"""
    status: "aws_sdk_m2.types.data_set_task_lifecycle.DataSetTaskLifecycle"
    """<p>The status of the data set import task.</p>"""
    summary: "aws_sdk_m2.types.data_set_import_summary.DataSetImportSummary"
    """<p>A summary of the data set import task.</p>"""
    status_reason: NotRequired["str"]
    """<p>If dataset import failed, the failure reason will show here.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetImportTask) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    out["status"] = value["status"]
    import aws_sdk_m2.types.data_set_import_summary

    out["summary"] = aws_sdk_m2.types.data_set_import_summary.serialize_json(
        value["summary"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> DataSetImportTask:
    out: DataSetImportTask = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("DataSetImportTask.task_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("DataSetImportTask.status required")
    if "summary" in data:
        import aws_sdk_m2.types.data_set_import_summary

        out["summary"] = aws_sdk_m2.types.data_set_import_summary.deserialize_json(
            data["summary"]
        )
    else:
        raise DeserializationError("DataSetImportTask.summary required")
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
