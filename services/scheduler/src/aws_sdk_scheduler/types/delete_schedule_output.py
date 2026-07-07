"""Generated from Smithy shape ``com.amazonaws.scheduler#DeleteScheduleOutput``."""

from typing_extensions import TypedDict


class DeleteScheduleOutput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DeleteScheduleOutput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteScheduleOutput:
    out: DeleteScheduleOutput = {}  # type: ignore[typeddict-item]
    return out
