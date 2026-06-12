"""Generated from Smithy shape ``com.amazonaws.medialive#ListEventBridgeRuleTemplatesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary
    import aws_sdk_medialive.types.__string_min1_max2048


class ListEventBridgeRuleTemplatesResponse(TypedDict):
    event_bridge_rule_templates: NotRequired[
        "aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary.__listOfEventBridgeRuleTemplateSummary"
    ]
    next_token: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventBridgeRuleTemplatesResponse) -> dict:
    out: dict = {}
    if "event_bridge_rule_templates" in value:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary

        out["eventBridgeRuleTemplates"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary.serialize_json(
                value["event_bridge_rule_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventBridgeRuleTemplatesResponse:
    out: ListEventBridgeRuleTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "eventBridgeRuleTemplates" in data:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary

        out["event_bridge_rule_templates"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_summary.deserialize_json(
                data["eventBridgeRuleTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
