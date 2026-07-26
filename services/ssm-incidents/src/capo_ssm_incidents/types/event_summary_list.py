"""Generated from Smithy shape ``com.amazonaws.ssmincidents#EventSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm_incidents.types.event_summary

EventSummaryList: TypeAlias = list[
    "capo_ssm_incidents.types.event_summary.EventSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventSummaryList) -> list:
    import capo_ssm_incidents.types.event_summary

    out: list = []
    for item in value:
        out.append(capo_ssm_incidents.types.event_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventSummaryList:
    import capo_ssm_incidents.types.event_summary

    out: EventSummaryList = []
    for item in data:
        out.append(capo_ssm_incidents.types.event_summary.deserialize_json(item))
    return out
