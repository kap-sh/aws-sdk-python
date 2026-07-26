"""Generated from Smithy shape ``com.amazonaws.oam#DeleteSinkOutput``."""

from typing_extensions import TypedDict


class DeleteSinkOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSinkOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSinkOutput:
    out: DeleteSinkOutput = {}  # type: ignore[typeddict-item]
    return out
