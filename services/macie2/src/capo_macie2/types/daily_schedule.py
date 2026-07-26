"""Generated from Smithy shape ``com.amazonaws.macie2#DailySchedule``."""

from typing_extensions import TypedDict


class DailySchedule(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DailySchedule) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DailySchedule:
    out: DailySchedule = {}  # type: ignore[typeddict-item]
    return out
