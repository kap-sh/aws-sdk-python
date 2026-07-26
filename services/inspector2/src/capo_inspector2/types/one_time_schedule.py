"""Generated from Smithy shape ``com.amazonaws.inspector2#OneTimeSchedule``."""

from typing_extensions import TypedDict


class OneTimeSchedule(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: OneTimeSchedule) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> OneTimeSchedule:
    out: OneTimeSchedule = {}  # type: ignore[typeddict-item]
    return out
