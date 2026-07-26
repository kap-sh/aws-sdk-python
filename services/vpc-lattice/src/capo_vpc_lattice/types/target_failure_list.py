"""Generated from Smithy shape ``com.amazonaws.vpclattice#TargetFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.target_failure

TargetFailureList: TypeAlias = list[
    "capo_vpc_lattice.types.target_failure.TargetFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: TargetFailureList) -> list:
    import capo_vpc_lattice.types.target_failure

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.target_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> TargetFailureList:
    import capo_vpc_lattice.types.target_failure

    out: TargetFailureList = []
    for item in data:
        out.append(capo_vpc_lattice.types.target_failure.deserialize_json(item))
    return out
