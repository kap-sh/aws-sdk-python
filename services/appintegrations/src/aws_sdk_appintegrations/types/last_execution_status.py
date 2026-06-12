"""Generated from Smithy shape ``com.amazonaws.appintegrations#LastExecutionStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.execution_status
    import aws_sdk_appintegrations.types.non_blank_string


class LastExecutionStatus(TypedDict):
    execution_status: NotRequired[
        "aws_sdk_appintegrations.types.execution_status.ExecutionStatus"
    ]
    """<p>The job status enum string.</p>"""
    status_message: NotRequired[
        "aws_sdk_appintegrations.types.non_blank_string.NonBlankString"
    ]
    """<p>The status message of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastExecutionStatus) -> dict:
    out: dict = {}
    if "execution_status" in value:
        import aws_sdk_appintegrations.types.execution_status

        out["ExecutionStatus"] = (
            aws_sdk_appintegrations.types.execution_status.serialize_json(
                value["execution_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> LastExecutionStatus:
    out: LastExecutionStatus = {}  # type: ignore[typeddict-item]
    if "ExecutionStatus" in data:
        import aws_sdk_appintegrations.types.execution_status

        out["execution_status"] = (
            aws_sdk_appintegrations.types.execution_status.deserialize_json(
                data["ExecutionStatus"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
