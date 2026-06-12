"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfEventBridgeRuleTemplateTarget``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.event_bridge_rule_template_target

__listOfEventBridgeRuleTemplateTarget: TypeAlias = list[
    "aws_sdk_medialive.types.event_bridge_rule_template_target.EventBridgeRuleTemplateTarget"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEventBridgeRuleTemplateTarget) -> list:
    import aws_sdk_medialive.types.event_bridge_rule_template_target

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.event_bridge_rule_template_target.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfEventBridgeRuleTemplateTarget:
    import aws_sdk_medialive.types.event_bridge_rule_template_target

    out: __listOfEventBridgeRuleTemplateTarget = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.event_bridge_rule_template_target.deserialize_json(
                item
            )
        )
    return out
