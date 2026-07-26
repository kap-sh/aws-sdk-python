"""Generated from Smithy shape ``com.amazonaws.medialive#ListEventBridgeRuleTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of_event_bridge_rule_template_summary
    import capo_medialive.types.__string_min1_max2048


class ListEventBridgeRuleTemplatesResponse(TypedDict, closed=True):
    event_bridge_rule_templates: NotRequired[
        "capo_medialive.types.__list_of_event_bridge_rule_template_summary.__listOfEventBridgeRuleTemplateSummary"
    ]
    next_token: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventBridgeRuleTemplatesResponse) -> dict:
    out: dict = {}
    if "event_bridge_rule_templates" in value:
        import capo_medialive.types.__list_of_event_bridge_rule_template_summary

        out["eventBridgeRuleTemplates"] = (
            capo_medialive.types.__list_of_event_bridge_rule_template_summary.serialize_json(
                value["event_bridge_rule_templates"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventBridgeRuleTemplatesResponse:
    out: ListEventBridgeRuleTemplatesResponse = {}  # type: ignore[typeddict-item]
    if "eventBridgeRuleTemplates" in data:
        import capo_medialive.types.__list_of_event_bridge_rule_template_summary

        out["event_bridge_rule_templates"] = (
            capo_medialive.types.__list_of_event_bridge_rule_template_summary.deserialize_json(
                data["eventBridgeRuleTemplates"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
