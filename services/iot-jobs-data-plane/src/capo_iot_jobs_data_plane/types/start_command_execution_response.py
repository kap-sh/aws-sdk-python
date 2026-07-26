"""Generated from Smithy shape ``com.amazonaws.iotjobsdataplane#StartCommandExecutionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_jobs_data_plane.types.command_execution_id


class StartCommandExecutionResponse(TypedDict, closed=True):
    execution_id: NotRequired[
        "capo_iot_jobs_data_plane.types.command_execution_id.CommandExecutionId"
    ]
    """<p>A unique identifier for the command execution.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartCommandExecutionResponse) -> dict:
    out: dict = {}
    if "execution_id" in value:
        out["executionId"] = value["execution_id"]
    return out


def deserialize_json(data: dict) -> StartCommandExecutionResponse:
    out: StartCommandExecutionResponse = {}  # type: ignore[typeddict-item]
    if "executionId" in data:
        out["execution_id"] = data["executionId"]
    return out
