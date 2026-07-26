"""Generated from Smithy shape ``com.amazonaws.networkmonitor#MonitorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmonitor.types.monitor_summary

MonitorList: TypeAlias = list[
    "capo_networkmonitor.types.monitor_summary.MonitorSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorList) -> list:
    import capo_networkmonitor.types.monitor_summary

    out: list = []
    for item in value:
        out.append(capo_networkmonitor.types.monitor_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> MonitorList:
    import capo_networkmonitor.types.monitor_summary

    out: MonitorList = []
    for item in data:
        out.append(capo_networkmonitor.types.monitor_summary.deserialize_json(item))
    return out
