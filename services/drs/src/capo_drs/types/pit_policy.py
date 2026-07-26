"""Generated from Smithy shape ``com.amazonaws.drs#PITPolicy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.pit_policy_rule

PITPolicy: TypeAlias = list["capo_drs.types.pit_policy_rule.PITPolicyRule"]


# --- restJson1 ser/de ---
def serialize_json(value: PITPolicy) -> list:
    import capo_drs.types.pit_policy_rule

    out: list = []
    for item in value:
        out.append(capo_drs.types.pit_policy_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> PITPolicy:
    import capo_drs.types.pit_policy_rule

    out: PITPolicy = []
    for item in data:
        out.append(capo_drs.types.pit_policy_rule.deserialize_json(item))
    return out
