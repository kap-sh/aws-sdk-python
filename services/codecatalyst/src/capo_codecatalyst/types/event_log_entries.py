"""Generated from Smithy shape ``com.amazonaws.codecatalyst#EventLogEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codecatalyst.types.event_log_entry

EventLogEntries: TypeAlias = list[
    "capo_codecatalyst.types.event_log_entry.EventLogEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventLogEntries) -> list:
    import capo_codecatalyst.types.event_log_entry

    out: list = []
    for item in value:
        out.append(capo_codecatalyst.types.event_log_entry.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventLogEntries:
    import capo_codecatalyst.types.event_log_entry

    out: EventLogEntries = []
    for item in data:
        out.append(capo_codecatalyst.types.event_log_entry.deserialize_json(item))
    return out
