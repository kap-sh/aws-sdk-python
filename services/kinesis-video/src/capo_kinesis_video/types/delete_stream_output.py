"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#DeleteStreamOutput``."""

from typing_extensions import TypedDict


class DeleteStreamOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteStreamOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteStreamOutput:
    out: DeleteStreamOutput = {}  # type: ignore[typeddict-item]
    return out
