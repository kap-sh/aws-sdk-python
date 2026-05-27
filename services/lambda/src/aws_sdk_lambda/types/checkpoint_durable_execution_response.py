"""Generated from Smithy shape ``com.amazonaws.lambda#CheckpointDurableExecutionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.checkpoint_token
    import aws_sdk_lambda.types.checkpoint_updated_execution_state


class CheckpointDurableExecutionResponse(TypedDict):
    checkpoint_token: NotRequired[
        "aws_sdk_lambda.types.checkpoint_token.CheckpointToken"
    ]
    """<p>A new checkpoint token to use for the next checkpoint operation. This token replaces the one provided in the request and must be used for subsequent checkpoints to maintain proper ordering.</p>"""
    new_execution_state: "aws_sdk_lambda.types.checkpoint_updated_execution_state.CheckpointUpdatedExecutionState"
    """<p>Updated execution state information that includes any changes that occurred since the last checkpoint, such as completed callbacks or expired timers. This allows the SDK to update its internal state during replay.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CheckpointDurableExecutionResponse) -> dict:
    out: dict = {}
    if "checkpoint_token" in value:
        out["CheckpointToken"] = value["checkpoint_token"]
    import aws_sdk_lambda.types.checkpoint_updated_execution_state

    out["NewExecutionState"] = (
        aws_sdk_lambda.types.checkpoint_updated_execution_state.serialize_json(
            value["new_execution_state"]
        )
    )
    return out


def deserialize_json(data: dict) -> CheckpointDurableExecutionResponse:
    out: CheckpointDurableExecutionResponse = {}  # type: ignore[typeddict-item]
    if "CheckpointToken" in data:
        out["checkpoint_token"] = data["CheckpointToken"]
    if "NewExecutionState" in data:
        import aws_sdk_lambda.types.checkpoint_updated_execution_state

        out["new_execution_state"] = (
            aws_sdk_lambda.types.checkpoint_updated_execution_state.deserialize_json(
                data["NewExecutionState"]
            )
        )
    else:
        raise DeserializationError(
            "CheckpointDurableExecutionResponse.new_execution_state required"
        )
    return out
