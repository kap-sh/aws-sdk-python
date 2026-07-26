"""Generated from Smithy shape ``com.amazonaws.appintegrations#LastExecutionStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.execution_status
    import capo_appintegrations.types.non_blank_string


class LastExecutionStatus(TypedDict, closed=True):
    execution_status: NotRequired[
        "capo_appintegrations.types.execution_status.ExecutionStatus"
    ]
    """<p>The job status enum string.</p>"""
    status_message: NotRequired[
        "capo_appintegrations.types.non_blank_string.NonBlankString"
    ]
    """<p>The status message of a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LastExecutionStatus) -> dict:
    out: dict = {}
    if "execution_status" in value:
        import capo_appintegrations.types.execution_status

        out["ExecutionStatus"] = (
            capo_appintegrations.types.execution_status.serialize_json(
                value["execution_status"]
            )
        )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> LastExecutionStatus:
    out: LastExecutionStatus = {}  # type: ignore[typeddict-item]
    if "ExecutionStatus" in data:
        import capo_appintegrations.types.execution_status

        out["execution_status"] = (
            capo_appintegrations.types.execution_status.deserialize_json(
                data["ExecutionStatus"]
            )
        )
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
