"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorLocalResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_local_resource

MonitorLocalResources: TypeAlias = list[
    "capo_networkflowmonitor.types.monitor_local_resource.MonitorLocalResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorLocalResources) -> list:
    import capo_networkflowmonitor.types.monitor_local_resource

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.monitor_local_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MonitorLocalResources:
    import capo_networkflowmonitor.types.monitor_local_resource

    out: MonitorLocalResources = []
    for item in data:
        out.append(
            capo_networkflowmonitor.types.monitor_local_resource.deserialize_json(item)
        )
    return out
