"""Generated from Smithy shape ``com.amazonaws.glue#ExecutionAttempt``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.description_string
    import aws_sdk_glue.types.execution_status
    import aws_sdk_glue.types.hash_string
    import aws_sdk_glue.types.timestamp


class ExecutionAttempt(TypedDict):
    status: NotRequired["aws_sdk_glue.types.execution_status.ExecutionStatus"]
    """<p>The status of the last column statistics task run.</p>"""
    column_statistics_task_run_id: NotRequired[
        "aws_sdk_glue.types.hash_string.HashString"
    ]
    """<p>A task run ID for the last column statistics task run.</p>"""
    execution_timestamp: NotRequired["aws_sdk_glue.types.timestamp.Timestamp"]
    """<p>A timestamp when the last column statistics task run occurred.</p>"""
    error_message: NotRequired[
        "aws_sdk_glue.types.description_string.DescriptionString"
    ]
    """<p>An error message associated with the last column statistics task run.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionAttempt) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_glue.types.execution_status

        out["Status"] = aws_sdk_glue.types.execution_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "column_statistics_task_run_id" in value:
        out["ColumnStatisticsTaskRunId"] = value["column_statistics_task_run_id"]
    if "execution_timestamp" in value:
        import aws_sdk_glue.types.timestamp

        out["ExecutionTimestamp"] = aws_sdk_glue.types.timestamp.serialize_aws_json_1_1(
            value["execution_timestamp"]
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionAttempt:
    out: ExecutionAttempt = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_glue.types.execution_status

        out["status"] = aws_sdk_glue.types.execution_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "ColumnStatisticsTaskRunId" in data:
        out["column_statistics_task_run_id"] = data["ColumnStatisticsTaskRunId"]
    if "ExecutionTimestamp" in data:
        import aws_sdk_glue.types.timestamp

        out["execution_timestamp"] = (
            aws_sdk_glue.types.timestamp.deserialize_aws_json_1_1(
                data["ExecutionTimestamp"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
