"""Generated from Smithy shape ``com.amazonaws.lambda#ErrorObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lambda.types.error_data
    import aws_sdk_lambda.types.error_message
    import aws_sdk_lambda.types.error_type
    import aws_sdk_lambda.types.stack_trace_entries


class ErrorObject(TypedDict):
    error_message: NotRequired["aws_sdk_lambda.types.error_message.ErrorMessage"]
    """<p>A human-readable error message.</p>"""
    error_type: NotRequired["aws_sdk_lambda.types.error_type.ErrorType"]
    """<p>The error type.</p>"""
    error_data: NotRequired["aws_sdk_lambda.types.error_data.ErrorData"]
    """<p>Machine-readable error data.</p>"""
    stack_trace: NotRequired[
        "aws_sdk_lambda.types.stack_trace_entries.StackTraceEntries"
    ]
    """<p>Stack trace information for the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorObject) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_data" in value:
        out["ErrorData"] = value["error_data"]
    if "stack_trace" in value:
        import aws_sdk_lambda.types.stack_trace_entries

        out["StackTrace"] = aws_sdk_lambda.types.stack_trace_entries.serialize_json(
            value["stack_trace"]
        )
    return out


def deserialize_json(data: dict) -> ErrorObject:
    out: ErrorObject = {}  # type: ignore[typeddict-item]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorData" in data:
        out["error_data"] = data["ErrorData"]
    if "StackTrace" in data:
        import aws_sdk_lambda.types.stack_trace_entries

        out["stack_trace"] = aws_sdk_lambda.types.stack_trace_entries.deserialize_json(
            data["StackTrace"]
        )
    return out
