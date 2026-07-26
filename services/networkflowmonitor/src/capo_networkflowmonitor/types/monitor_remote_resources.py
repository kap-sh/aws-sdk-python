"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#MonitorRemoteResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.monitor_remote_resource

MonitorRemoteResources: TypeAlias = list[
    "capo_networkflowmonitor.types.monitor_remote_resource.MonitorRemoteResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitorRemoteResources) -> list:
    import capo_networkflowmonitor.types.monitor_remote_resource

    out: list = []
    for item in value:
        out.append(
            capo_networkflowmonitor.types.monitor_remote_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MonitorRemoteResources:
    import capo_networkflowmonitor.types.monitor_remote_resource

    out: MonitorRemoteResources = []
    for item in data:
        out.append(
            capo_networkflowmonitor.types.monitor_remote_resource.deserialize_json(item)
        )
    return out
