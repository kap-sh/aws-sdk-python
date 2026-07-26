"""Generated from Smithy shape ``com.amazonaws.outposts#DeleteOutpostOutput``."""

from typing_extensions import TypedDict


class DeleteOutpostOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteOutpostOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteOutpostOutput:
    out: DeleteOutpostOutput = {}  # type: ignore[typeddict-item]
    return out
