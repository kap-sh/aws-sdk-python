"""Generated from Smithy shape ``com.amazonaws.datazone#LineageSyncSchedule``."""

from typing_extensions import NotRequired, TypedDict


class LineageSyncSchedule(TypedDict, closed=True):
    schedule: NotRequired["str"]
    """<p>The lineage sync schedule.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageSyncSchedule) -> dict:
    out: dict = {}
    if "schedule" in value:
        out["schedule"] = value["schedule"]
    return out


def deserialize_json(data: dict) -> LineageSyncSchedule:
    out: LineageSyncSchedule = {}  # type: ignore[typeddict-item]
    if "schedule" in data:
        out["schedule"] = data["schedule"]
    return out
