"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineVersionOutput``."""

from typing_extensions import TypedDict


class DeleteStateMachineVersionOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineVersionOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineVersionOutput:
    out: DeleteStateMachineVersionOutput = {}  # type: ignore[typeddict-item]
    return out
