"""Generated from Smithy shape ``com.amazonaws.devopsagent#DeregisterServiceOutput``."""

from typing_extensions import TypedDict


class DeregisterServiceOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterServiceOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeregisterServiceOutput:
    out: DeregisterServiceOutput = {}  # type: ignore[typeddict-item]
    return out
