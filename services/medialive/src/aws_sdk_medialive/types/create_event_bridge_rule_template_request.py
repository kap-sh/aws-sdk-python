"""Generated from Smithy shape ``com.amazonaws.medialive#CreateEventBridgeRuleTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_min1_max256_pattern_s
    import aws_sdk_medialive.types.__string_pattern_s
    import aws_sdk_medialive.types.event_bridge_rule_template_event_type
    import aws_sdk_medialive.types.tag_map


class CreateEventBridgeRuleTemplateRequest(TypedDict, closed=True):
    description: NotRequired[
        "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    event_targets: NotRequired[
        "aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target.__listOfEventBridgeRuleTemplateTarget"
    ]
    event_type: NotRequired[
        "aws_sdk_medialive.types.event_bridge_rule_template_event_type.EventBridgeRuleTemplateEventType"
    ]
    group_identifier: NotRequired[
        "aws_sdk_medialive.types.__string_pattern_s.__stringPatternS"
    ]
    """An eventbridge rule template group's identifier. Can be either be its id or current name."""
    name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    tags: NotRequired["aws_sdk_medialive.types.tag_map.TagMap"]
    request_id: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max256_pattern_s.__stringMin1Max256PatternS"
    ]
    """An ID that you assign to a create request. This ID ensures idempotency when creating resources."""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventBridgeRuleTemplateRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "event_targets" in value:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target

        out["eventTargets"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target.serialize_json(
                value["event_targets"]
            )
        )
    if "event_type" in value:
        import aws_sdk_medialive.types.event_bridge_rule_template_event_type

        out["eventType"] = (
            aws_sdk_medialive.types.event_bridge_rule_template_event_type.serialize_json(
                value["event_type"]
            )
        )
    if "group_identifier" in value:
        out["groupIdentifier"] = value["group_identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.serialize_json(value["tags"])
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateEventBridgeRuleTemplateRequest:
    out: CreateEventBridgeRuleTemplateRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "eventTargets" in data:
        import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target

        out["event_targets"] = (
            aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target.deserialize_json(
                data["eventTargets"]
            )
        )
    if "eventType" in data:
        import aws_sdk_medialive.types.event_bridge_rule_template_event_type

        out["event_type"] = (
            aws_sdk_medialive.types.event_bridge_rule_template_event_type.deserialize_json(
                data["eventType"]
            )
        )
    if "groupIdentifier" in data:
        out["group_identifier"] = data["groupIdentifier"]
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    return out
