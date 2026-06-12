"""Generated from Smithy shape ``com.amazonaws.appflow#ErrorInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.execution_message
    import aws_sdk_appflow.types.long


class ErrorInfo(TypedDict):
    put_failures_count: NotRequired["aws_sdk_appflow.types.long.Long"]
    """<p> Specifies the failure count for the attempted flow. </p>"""
    execution_message: NotRequired[
        "aws_sdk_appflow.types.execution_message.ExecutionMessage"
    ]
    """<p> Specifies the error message that appears if a flow fails. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorInfo) -> dict:
    out: dict = {}
    if "put_failures_count" in value:
        out["putFailuresCount"] = value["put_failures_count"]
    if "execution_message" in value:
        out["executionMessage"] = value["execution_message"]
    return out


def deserialize_json(data: dict) -> ErrorInfo:
    out: ErrorInfo = {}  # type: ignore[typeddict-item]
    if "putFailuresCount" in data:
        out["put_failures_count"] = data["putFailuresCount"]
    if "executionMessage" in data:
        out["execution_message"] = data["executionMessage"]
    return out
