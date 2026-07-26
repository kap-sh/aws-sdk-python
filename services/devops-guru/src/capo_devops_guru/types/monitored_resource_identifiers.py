"""Generated from Smithy shape ``com.amazonaws.devopsguru#MonitoredResourceIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.monitored_resource_identifier

MonitoredResourceIdentifiers: TypeAlias = list[
    "capo_devops_guru.types.monitored_resource_identifier.MonitoredResourceIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: MonitoredResourceIdentifiers) -> list:
    import capo_devops_guru.types.monitored_resource_identifier

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.monitored_resource_identifier.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MonitoredResourceIdentifiers:
    import capo_devops_guru.types.monitored_resource_identifier

    out: MonitoredResourceIdentifiers = []
    for item in data:
        out.append(
            capo_devops_guru.types.monitored_resource_identifier.deserialize_json(item)
        )
    return out
