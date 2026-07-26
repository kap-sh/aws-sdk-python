"""Generated from Smithy shape ``com.amazonaws.datazone#RemovePolicyGrantOutput``."""

from typing_extensions import TypedDict


class RemovePolicyGrantOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RemovePolicyGrantOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RemovePolicyGrantOutput:
    out: RemovePolicyGrantOutput = {}  # type: ignore[typeddict-item]
    return out
