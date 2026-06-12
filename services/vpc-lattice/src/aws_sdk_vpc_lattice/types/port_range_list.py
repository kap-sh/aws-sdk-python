"""Generated from Smithy shape ``com.amazonaws.vpclattice#PortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.port_range

PortRangeList: TypeAlias = list["aws_sdk_vpc_lattice.types.port_range.PortRange"]


# --- restJson1 ser/de ---
def serialize_json(value: PortRangeList) -> list:
    return list(value)


def deserialize_json(data: list) -> PortRangeList:
    return list(data)
