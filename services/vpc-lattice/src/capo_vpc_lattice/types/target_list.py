"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target

TargetList: TypeAlias = list["capo_vpc_lattice.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: TargetList) -> list:
    import capo_vpc_lattice.types.target

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.target.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetList:
    import capo_vpc_lattice.types.target

    out: TargetList = []
    for item in data:
        out.append(capo_vpc_lattice.types.target.deserialize_json(item))
    return out
