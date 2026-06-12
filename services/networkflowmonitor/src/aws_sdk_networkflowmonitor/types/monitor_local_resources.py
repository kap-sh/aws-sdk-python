"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResources``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_networkflowmonitor.types.monitor_local_resource

MonitorLocalResources: TypeAlias = list["aws_sdk_networkflowmonitor.types.monitor_local_resource.MonitorLocalResource"]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorLocalResources) -> list:
    import aws_sdk_networkflowmonitor.types.monitor_local_resource
    out: list = []
    for item in value:
        out.append(aws_sdk_networkflowmonitor.types.monitor_local_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> MonitorLocalResources:
    import aws_sdk_networkflowmonitor.types.monitor_local_resource
    out: MonitorLocalResources = []
    for item in data:
        out.append(aws_sdk_networkflowmonitor.types.monitor_local_resource.deserialize_json(item))
    return out