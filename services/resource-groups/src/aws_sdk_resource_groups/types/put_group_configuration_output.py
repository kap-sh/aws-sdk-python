"""Generated from Smithy shape ``com.amazonaws.resourcegroups#PutGroupConfigurationOutput``."""

from typing_extensions import TypedDict


class PutGroupConfigurationOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutGroupConfigurationOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutGroupConfigurationOutput:
    out: PutGroupConfigurationOutput = {}  # type: ignore[typeddict-item]
    return out
