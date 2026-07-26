"""Generated from Smithy shape ``com.amazonaws.internetmonitor#InternetEventsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_internetmonitor.types.internet_event_summary

InternetEventsList: TypeAlias = list[
    "capo_internetmonitor.types.internet_event_summary.InternetEventSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: InternetEventsList) -> list:
    import capo_internetmonitor.types.internet_event_summary

    out: list = []
    for item in value:
        out.append(
            capo_internetmonitor.types.internet_event_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InternetEventsList:
    import capo_internetmonitor.types.internet_event_summary

    out: InternetEventsList = []
    for item in data:
        out.append(
            capo_internetmonitor.types.internet_event_summary.deserialize_json(item)
        )
    return out
