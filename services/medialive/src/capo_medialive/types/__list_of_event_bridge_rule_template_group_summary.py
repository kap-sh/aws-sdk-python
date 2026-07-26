"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfEventBridgeRuleTemplateGroupSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.event_bridge_rule_template_group_summary

__listOfEventBridgeRuleTemplateGroupSummary: TypeAlias = list[
    "capo_medialive.types.event_bridge_rule_template_group_summary.EventBridgeRuleTemplateGroupSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEventBridgeRuleTemplateGroupSummary) -> list:
    import capo_medialive.types.event_bridge_rule_template_group_summary

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.event_bridge_rule_template_group_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfEventBridgeRuleTemplateGroupSummary:
    import capo_medialive.types.event_bridge_rule_template_group_summary

    out: __listOfEventBridgeRuleTemplateGroupSummary = []
    for item in data:
        out.append(
            capo_medialive.types.event_bridge_rule_template_group_summary.deserialize_json(
                item
            )
        )
    return out
