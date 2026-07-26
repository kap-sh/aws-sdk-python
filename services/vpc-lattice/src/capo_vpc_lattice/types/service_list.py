"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_summary

ServiceList: TypeAlias = list["capo_vpc_lattice.types.service_summary.ServiceSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceList) -> list:
    import capo_vpc_lattice.types.service_summary

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.service_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ServiceList:
    import capo_vpc_lattice.types.service_summary

    out: ServiceList = []
    for item in data:
        out.append(capo_vpc_lattice.types.service_summary.deserialize_json(item))
    return out
