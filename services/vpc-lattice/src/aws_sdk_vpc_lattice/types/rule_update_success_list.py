"""Generated from Smithy shape ``com.amazonaws.vpclattice#RuleUpdateSuccessList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_vpc_lattice.types.rule_update_success

RuleUpdateSuccessList: TypeAlias = list[
    "aws_sdk_vpc_lattice.types.rule_update_success.RuleUpdateSuccess"
]


# --- restJson1 ser/de ---
def serialize_json(value: RuleUpdateSuccessList) -> list:
    import aws_sdk_vpc_lattice.types.rule_update_success

    out: list = []
    for item in value:
        out.append(aws_sdk_vpc_lattice.types.rule_update_success.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleUpdateSuccessList:
    import aws_sdk_vpc_lattice.types.rule_update_success

    out: RuleUpdateSuccessList = []
    for item in data:
        out.append(aws_sdk_vpc_lattice.types.rule_update_success.deserialize_json(item))
    return out
