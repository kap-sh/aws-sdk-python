"""Generated from Smithy shape ``com.amazonaws.connect#RuleActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.rule_action

RuleActions: TypeAlias = list["capo_connect.types.rule_action.RuleAction"]


# --- restJson1 ser/de ---
def serialize_json(value: RuleActions) -> list:
    import capo_connect.types.rule_action

    out: list = []
    for item in value:
        out.append(capo_connect.types.rule_action.serialize_json(item))
    return out


def deserialize_json(data: list) -> RuleActions:
    import capo_connect.types.rule_action

    out: RuleActions = []
    for item in data:
        out.append(capo_connect.types.rule_action.deserialize_json(item))
    return out
