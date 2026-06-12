"""Generated from Smithy shape ``com.amazonaws.networkmonitor#CreateMonitorProbeInputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmonitor.types.create_monitor_probe_input

CreateMonitorProbeInputList: TypeAlias = list[
    "aws_sdk_networkmonitor.types.create_monitor_probe_input.CreateMonitorProbeInput"
]


# --- restJson1 ser/de ---
def serialize_json(value: CreateMonitorProbeInputList) -> list:
    import aws_sdk_networkmonitor.types.create_monitor_probe_input

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmonitor.types.create_monitor_probe_input.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CreateMonitorProbeInputList:
    import aws_sdk_networkmonitor.types.create_monitor_probe_input

    out: CreateMonitorProbeInputList = []
    for item in data:
        out.append(
            aws_sdk_networkmonitor.types.create_monitor_probe_input.deserialize_json(
                item
            )
        )
    return out
