"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#ImportBatch``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cloudwatch_logs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_logs.types.batch_id
    import aws_sdk_cloudwatch_logs.types.error_message
    import aws_sdk_cloudwatch_logs.types.import_status


class ImportBatch(TypedDict, closed=True):
    batch_id: "aws_sdk_cloudwatch_logs.types.batch_id.BatchId"
    """<p>The unique identifier of the import batch.</p>"""
    status: "aws_sdk_cloudwatch_logs.types.import_status.ImportStatus"
    """<p>The current status of the import batch. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>"""
    error_message: NotRequired[
        "aws_sdk_cloudwatch_logs.types.error_message.ErrorMessage"
    ]
    """<p>The error message if the batch failed to import. Only present when status is FAILED.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportBatch) -> dict:
    out: dict = {}
    out["batchId"] = value["batch_id"]
    import aws_sdk_cloudwatch_logs.types.import_status

    out["status"] = aws_sdk_cloudwatch_logs.types.import_status.serialize_aws_json_1_1(
        value["status"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportBatch:
    out: ImportBatch = {}  # type: ignore[typeddict-item]
    if "batchId" in data:
        out["batch_id"] = data["batchId"]
    else:
        raise DeserializationError("ImportBatch.batch_id required")
    if "status" in data:
        import aws_sdk_cloudwatch_logs.types.import_status

        out["status"] = (
            aws_sdk_cloudwatch_logs.types.import_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    else:
        raise DeserializationError("ImportBatch.status required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
