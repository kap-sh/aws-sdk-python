"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.arn


class DeleteStateMachineInput(TypedDict, closed=True):
    state_machine_arn: "aws_sdk_sfn.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the state machine to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineInput) -> dict:
    out: dict = {}
    out["stateMachineArn"] = value["state_machine_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineInput:
    out: DeleteStateMachineInput = {}  # type: ignore[typeddict-item]
    if "stateMachineArn" in data:
        out["state_machine_arn"] = data["stateMachineArn"]
    else:
        raise DeserializationError("DeleteStateMachineInput.state_machine_arn required")
    return out
