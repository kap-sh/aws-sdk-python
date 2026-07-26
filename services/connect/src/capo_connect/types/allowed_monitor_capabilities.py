"""Generated from Smithy shape ``com.amazonaws.connect#AllowedMonitorCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.monitor_capability

AllowedMonitorCapabilities: TypeAlias = list[
    "capo_connect.types.monitor_capability.MonitorCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedMonitorCapabilities) -> list:
    import capo_connect.types.monitor_capability

    out: list = []
    for item in value:
        out.append(capo_connect.types.monitor_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedMonitorCapabilities:
    import capo_connect.types.monitor_capability

    out: AllowedMonitorCapabilities = []
    for item in data:
        out.append(capo_connect.types.monitor_capability.deserialize_json(item))
    return out
