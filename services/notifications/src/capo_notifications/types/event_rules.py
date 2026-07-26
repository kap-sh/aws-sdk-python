"""Generated from Smithy shape ``com.amazonaws.notifications#EventRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_notifications.types.event_rule_structure

EventRules: TypeAlias = list[
    "capo_notifications.types.event_rule_structure.EventRuleStructure"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventRules) -> list:
    import capo_notifications.types.event_rule_structure

    out: list = []
    for item in value:
        out.append(capo_notifications.types.event_rule_structure.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventRules:
    import capo_notifications.types.event_rule_structure

    out: EventRules = []
    for item in data:
        out.append(capo_notifications.types.event_rule_structure.deserialize_json(item))
    return out
