"""Generated from Smithy shape ``com.amazonaws.sfn#DeleteStateMachineAliasOutput``."""

from typing_extensions import TypedDict


class DeleteStateMachineAliasOutput(TypedDict, closed=True):
    pass


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteStateMachineAliasOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteStateMachineAliasOutput:
    out: DeleteStateMachineAliasOutput = {}  # type: ignore[typeddict-item]
    return out
