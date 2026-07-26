"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineOutput``."""

from typing_extensions import TypedDict


class DeleteStateMachineOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineOutput:
    out: DeleteStateMachineOutput = {}  # type: ignore[typeddict-item]
    return out
