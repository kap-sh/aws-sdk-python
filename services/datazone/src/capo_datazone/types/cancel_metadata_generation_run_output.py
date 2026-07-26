"""Generated from Smithy shape ``com.amazonaws.datazone#CancelMetadataGenerationRunOutput``."""

from typing_extensions import TypedDict


class CancelMetadataGenerationRunOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelMetadataGenerationRunOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMetadataGenerationRunOutput:
    out: CancelMetadataGenerationRunOutput = {}  # type: ignore[typeddict-item]
    return out
