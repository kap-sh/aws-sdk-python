"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetExportTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.data_set_export_summary
    import aws_sdk_m2.types.data_set_task_lifecycle
    import aws_sdk_m2.types.identifier


class GetDataSetExportTaskResponse(TypedDict, closed=True):
    task_id: "aws_sdk_m2.types.identifier.Identifier"
    """<p>The task identifier.</p>"""
    status: "aws_sdk_m2.types.data_set_task_lifecycle.DataSetTaskLifecycle"
    """<p>The status of the task.</p>"""
    summary: NotRequired[
        "aws_sdk_m2.types.data_set_export_summary.DataSetExportSummary"
    ]
    """<p>A summary of the status of the task.</p>"""
    status_reason: NotRequired["str"]
    """<p>If dataset export failed, the failure reason will show here.</p>"""
    kms_key_arn: NotRequired["str"]
    """<p>The identifier of a customer managed key used for exported data set encryption.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetExportTaskResponse) -> dict:
    out: dict = {}
    out["taskId"] = value["task_id"]
    out["status"] = value["status"]
    if "summary" in value:
        import aws_sdk_m2.types.data_set_export_summary

        out["summary"] = aws_sdk_m2.types.data_set_export_summary.serialize_json(
            value["summary"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetDataSetExportTaskResponse:
    out: GetDataSetExportTaskResponse = {}  # type: ignore[typeddict-item]
    if "taskId" in data:
        out["task_id"] = data["taskId"]
    else:
        raise DeserializationError("GetDataSetExportTaskResponse.task_id required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("GetDataSetExportTaskResponse.status required")
    if "summary" in data:
        import aws_sdk_m2.types.data_set_export_summary

        out["summary"] = aws_sdk_m2.types.data_set_export_summary.deserialize_json(
            data["summary"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
