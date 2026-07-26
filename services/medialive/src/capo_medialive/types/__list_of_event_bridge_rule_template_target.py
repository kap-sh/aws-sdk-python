"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfEventBridgeRuleTemplateTarget``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.event_bridge_rule_template_target

__listOfEventBridgeRuleTemplateTarget: TypeAlias = list[
    "capo_medialive.types.event_bridge_rule_template_target.EventBridgeRuleTemplateTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEventBridgeRuleTemplateTarget) -> list:
    import capo_medialive.types.event_bridge_rule_template_target

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.event_bridge_rule_template_target.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfEventBridgeRuleTemplateTarget:
    import capo_medialive.types.event_bridge_rule_template_target

    out: __listOfEventBridgeRuleTemplateTarget = []
    for item in data:
        out.append(
            capo_medialive.types.event_bridge_rule_template_target.deserialize_json(
                item
            )
        )
    return out
