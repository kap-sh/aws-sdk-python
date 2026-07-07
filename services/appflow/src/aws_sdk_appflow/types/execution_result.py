"""Generated from Smithy shape ``com.amazonaws.appflow#ExecutionResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_info
    import aws_sdk_appflow.types.long


class ExecutionResult(TypedDict, closed=True):
    error_info: NotRequired["aws_sdk_appflow.types.error_info.ErrorInfo"]
    """<p> Provides any error message information related to the flow run. </p>"""
    bytes_processed: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p> The total number of bytes processed by the flow run. </p>"""
    bytes_written: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p> The total number of bytes written as a result of the flow run. </p>"""
    records_processed: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p> The number of records processed in the flow run. </p>"""
    num_parallel_processes: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p>The number of processes that Amazon AppFlow ran at the same time when it retrieved your data.</p>"""
    max_page_size: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p>The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionResult) -> dict:
    out: dict = {}
    if "error_info" in value:
        import aws_sdk_appflow.types.error_info

        out["errorInfo"] = aws_sdk_appflow.types.error_info.serialize_json(
            value["error_info"]
        )
    if "bytes_processed" in value:
        out["bytesProcessed"] = value["bytes_processed"]
    if "bytes_written" in value:
        out["bytesWritten"] = value["bytes_written"]
    if "records_processed" in value:
        out["recordsProcessed"] = value["records_processed"]
    if "num_parallel_processes" in value:
        out["numParallelProcesses"] = value["num_parallel_processes"]
    if "max_page_size" in value:
        out["maxPageSize"] = value["max_page_size"]
    return out


def deserialize_json(data: dict) -> ExecutionResult:
    out: ExecutionResult = {}  # type: ignore[typeddict-item]
    if "errorInfo" in data:
        import aws_sdk_appflow.types.error_info

        out["error_info"] = aws_sdk_appflow.types.error_info.deserialize_json(
            data["errorInfo"]
        )
    if "bytesProcessed" in data:
        out["bytes_processed"] = data["bytesProcessed"]
    if "bytesWritten" in data:
        out["bytes_written"] = data["bytesWritten"]
    if "recordsProcessed" in data:
        out["records_processed"] = data["recordsProcessed"]
    if "numParallelProcesses" in data:
        out["num_parallel_processes"] = data["numParallelProcesses"]
    if "maxPageSize" in data:
        out["max_page_size"] = data["maxPageSize"]
    return out
