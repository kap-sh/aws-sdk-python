"""Generated from Smithy shape ``com.amazonaws.internetmonitor#MonitorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_internetmonitor.types.monitor

MonitorList: TypeAlias = list["capo_internetmonitor.types.monitor.Monitor"]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorList) -> list:
    import capo_internetmonitor.types.monitor

    out: list = []
    for item in value:
        out.append(capo_internetmonitor.types.monitor.serialize_json(item))
    return out


def deserialize_json(data: list) -> MonitorList:
    import capo_internetmonitor.types.monitor

    out: MonitorList = []
    for item in data:
        out.append(capo_internetmonitor.types.monitor.deserialize_json(item))
    return out
