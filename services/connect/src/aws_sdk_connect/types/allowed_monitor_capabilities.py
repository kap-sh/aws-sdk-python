"""Generated from Smithy shape ``com.amazonaws.connect#AllowedMonitorCapabilities``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.monitor_capability

AllowedMonitorCapabilities: TypeAlias = list[
    "aws_sdk_connect.types.monitor_capability.MonitorCapability"
]


# --- restJson1 ser/de ---
def serialize_json(value: AllowedMonitorCapabilities) -> list:
    import aws_sdk_connect.types.monitor_capability

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.monitor_capability.serialize_json(item))
    return out


def deserialize_json(data: list) -> AllowedMonitorCapabilities:
    import aws_sdk_connect.types.monitor_capability

    out: AllowedMonitorCapabilities = []
    for item in data:
        out.append(aws_sdk_connect.types.monitor_capability.deserialize_json(item))
    return out
