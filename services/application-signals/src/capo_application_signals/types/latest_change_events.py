"""Generated from Smithy shape ``com.amazonaws.applicationsignals#LatestChangeEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.change_event

LatestChangeEvents: TypeAlias = list[
    "capo_application_signals.types.change_event.ChangeEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: LatestChangeEvents) -> list:
    import capo_application_signals.types.change_event

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.change_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> LatestChangeEvents:
    import capo_application_signals.types.change_event

    out: LatestChangeEvents = []
    for item in data:
        out.append(capo_application_signals.types.change_event.deserialize_json(item))
    return out
