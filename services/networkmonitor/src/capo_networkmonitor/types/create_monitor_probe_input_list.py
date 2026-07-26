"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorProbeInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmonitor.types.create_monitor_probe_input

CreateMonitorProbeInputList: TypeAlias = list[
    "capo_networkmonitor.types.create_monitor_probe_input.CreateMonitorProbeInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorProbeInputList) -> list:
    import capo_networkmonitor.types.create_monitor_probe_input

    out: list = []
    for item in value:
        out.append(
            capo_networkmonitor.types.create_monitor_probe_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateMonitorProbeInputList:
    import capo_networkmonitor.types.create_monitor_probe_input

    out: CreateMonitorProbeInputList = []
    for item in data:
        out.append(
            capo_networkmonitor.types.create_monitor_probe_input.deserialize_json(item)
        )
    return out
