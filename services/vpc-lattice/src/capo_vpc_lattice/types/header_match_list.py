"""Generated from Smithy shape ``com.amazonaws.vpclattice#HeaderMatchList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.header_match

HeaderMatchList: TypeAlias = list["capo_vpc_lattice.types.header_match.HeaderMatch"]


# --- restJson1 ser/de ---
def serialize_json(value: HeaderMatchList) -> list:
    import capo_vpc_lattice.types.header_match

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.header_match.serialize_json(item))
    return out


def deserialize_json(data: list) -> HeaderMatchList:
    import capo_vpc_lattice.types.header_match

    out: HeaderMatchList = []
    for item in data:
        out.append(capo_vpc_lattice.types.header_match.deserialize_json(item))
    return out
