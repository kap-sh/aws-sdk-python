"""Generated from Smithy shape ``com.amazonaws.medialive#ListEventBridgeRuleTemplateGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary
    import aws_sdk_medialive.types.__string_min1_max2048


class ListEventBridgeRuleTemplateGroupsResponse(TypedDict, closed=True):
    event_bridge_rule_template_groups: NotRequired[
        "aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary.__listOfEventBridgeRuleTemplateGroupSummary"
    ]
    next_token: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A token used to retrieve the next set of results in paginated list responses."""


# --- restJson1 ser/de ---
def serialize_json(value: ListEventBridgeRuleTemplateGroupsResponse) -> dict:
    out: dict = {}
    if "event_bridge_rule_template_groups" in value:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary

        out["eventBridgeRuleTemplateGroups"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary.serialize_json(
                value["event_bridge_rule_template_groups"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEventBridgeRuleTemplateGroupsResponse:
    out: ListEventBridgeRuleTemplateGroupsResponse = {}  # type: ignore[typeddict-item]
    if "eventBridgeRuleTemplateGroups" in data:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary

        out["event_bridge_rule_template_groups"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_group_summary.deserialize_json(
                data["eventBridgeRuleTemplateGroups"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
