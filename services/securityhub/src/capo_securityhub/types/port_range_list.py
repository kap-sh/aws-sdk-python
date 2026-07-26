"""Generated from Smithy shape ``com.amazonaws.securityhub#PortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.port_range

PortRangeList: TypeAlias = list["capo_securityhub.types.port_range.PortRange"]


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeList) -> list:
    import capo_securityhub.types.port_range

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.port_range.serialize_json(item))
    return out


def deserialize_json(data: list) -> PortRangeList:
    import capo_securityhub.types.port_range

    out: PortRangeList = []
    for item in data:
        out.append(capo_securityhub.types.port_range.deserialize_json(item))
    return out
