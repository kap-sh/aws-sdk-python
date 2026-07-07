"""Generated from Smithy shape ``com.amazonaws.bedrockagent#OutputFlowNodeConfiguration``."""

from typing_extensions import TypedDict


class OutputFlowNodeConfiguration(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: OutputFlowNodeConfiguration) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> OutputFlowNodeConfiguration:
    out: OutputFlowNodeConfiguration = {}  # type: ignore[typeddict-item]
    return out
