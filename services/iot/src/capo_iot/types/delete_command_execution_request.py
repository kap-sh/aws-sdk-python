"""Generated from Smithy shape ``com.amazonaws.iot#DeleteCommandExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.command_execution_id
    import capo_iot.types.target_arn


class DeleteCommandExecutionRequest(TypedDict, closed=True):
    execution_id: "capo_iot.types.command_execution_id.CommandExecutionId"
    """<p>The unique identifier of the command execution that you want to delete from your account.</p>"""
    target_arn: "capo_iot.types.target_arn.TargetArn"
    """<p>The Amazon Resource Number (ARN) of the target device for which you want to delete command executions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCommandExecutionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCommandExecutionRequest:
    out: DeleteCommandExecutionRequest = {}  # type: ignore[typeddict-item]
    return out
