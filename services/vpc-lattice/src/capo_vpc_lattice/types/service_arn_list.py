"""Generated from Smithy shape ``com.amazonaws.vpclattice#ServiceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.service_arn

ServiceArnList: TypeAlias = list["capo_vpc_lattice.types.service_arn.ServiceArn"]


# --- restJson1 ser/de ---
def serialize_json(value: ServiceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ServiceArnList:
    return list(data)
