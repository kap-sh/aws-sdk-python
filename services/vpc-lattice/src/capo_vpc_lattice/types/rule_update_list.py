"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_vpc_lattice.types.rule_update

RuleUpdateList: TypeAlias = list["capo_vpc_lattice.types.rule_update.RuleUpdate"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdateList) -> list:
    import capo_vpc_lattice.types.rule_update

    out: list = []
    for item in value:
        out.append(capo_vpc_lattice.types.rule_update.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleUpdateList:
    import capo_vpc_lattice.types.rule_update

    out: RuleUpdateList = []
    for item in data:
        out.append(capo_vpc_lattice.types.rule_update.deserialize_json(item))
    return out
