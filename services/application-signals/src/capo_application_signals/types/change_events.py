"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ChangeEvents``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_signals.types.change_event

ChangeEvents: TypeAlias = list[
    "capo_application_signals.types.change_event.ChangeEvent"
]


# --- restJson1 ser/de ---
def serialize_json(value: ChangeEvents) -> list:
    import capo_application_signals.types.change_event

    out: list = []
    for item in value:
        out.append(capo_application_signals.types.change_event.serialize_json(item))
    return out


def deserialize_json(data: list) -> ChangeEvents:
    import capo_application_signals.types.change_event

    out: ChangeEvents = []
    for item in data:
        out.append(capo_application_signals.types.change_event.deserialize_json(item))
    return out
