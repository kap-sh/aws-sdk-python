"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdateFailureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.rule_update_failure

RuleUpdateFailureList: TypeAlias = list[
    "capo_vpc_lattice.types.rule_update_failure.RuleUpdateFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdateFailureList) -> list:
    import capo_vpc_lattice.types.rule_update_failure

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.rule_update_failure.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleUpdateFailureList:
    import capo_vpc_lattice.types.rule_update_failure

    out: RuleUpdateFailureList = []
    for item in data:
        out.append(capo_vpc_lattice.types.rule_update_failure.deserialize_json(item))
    return out
