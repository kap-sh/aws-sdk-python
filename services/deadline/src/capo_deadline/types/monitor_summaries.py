"""Generated from Smithy shape ``com.amazonaws.deadline#MonitorSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.monitor_summary

MonitorSummaries: TypeAlias = list["capo_deadline.types.monitor_summary.MonitorSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorSummaries) -> list:
    import capo_deadline.types.monitor_summary

    out: list = []
    for item in value:
        out.append(capo_deadline.types.monitor_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MonitorSummaries:
    import capo_deadline.types.monitor_summary

    out: MonitorSummaries = []
    for item in data:
        out.append(capo_deadline.types.monitor_summary.deserialize_json(item))
    return out
