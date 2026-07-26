"""Generated from Smithy shape ``com.amazonaws.devopsagent#PortRanges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_agent.types.port_range

PortRanges: TypeAlias = list["capo_devops_agent.types.port_range.PortRange"]


# --- restJson1 ser/de ---
def serialize_json(value: PortRanges) -> list:
    return list(value)


def deserialize_json(data: list) -> PortRanges:
    return list(data)
