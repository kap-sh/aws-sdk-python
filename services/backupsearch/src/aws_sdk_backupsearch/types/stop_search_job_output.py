"""Generated from Smithy shape ``com.amazonaws.backupsearch#StopSearchJobOutput``."""

from typing_extensions import TypedDict


class StopSearchJobOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: StopSearchJobOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopSearchJobOutput:
    out: StopSearchJobOutput = {}  # type: ignore[typeddict-item]
    return out
