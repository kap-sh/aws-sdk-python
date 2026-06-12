"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfEventBridgeRuleTemplateSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.event_bridge_rule_template_summary

__listOfEventBridgeRuleTemplateSummary: TypeAlias = list[
    "aws_sdk_medialive.types.event_bridge_rule_template_summary.EventBridgeRuleTemplateSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfEventBridgeRuleTemplateSummary) -> list:
    import aws_sdk_medialive.types.event_bridge_rule_template_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_medialive.types.event_bridge_rule_template_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfEventBridgeRuleTemplateSummary:
    import aws_sdk_medialive.types.event_bridge_rule_template_summary

    out: __listOfEventBridgeRuleTemplateSummary = []
    for item in data:
        out.append(
            aws_sdk_medialive.types.event_bridge_rule_template_summary.deserialize_json(
                item
            )
        )
    return out
