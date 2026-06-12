"""Generated from Smithy shape ``com.amazonaws.medialive#UpdateEventBridgeRuleTemplateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_event_bridge_rule_template_target
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_min7_max11_pattern_aws097
    import aws_sdk_medialive.types.__string_pattern_arn_medialive_eventbridge_rule_template
    import aws_sdk_medialive.types.__timestamp_iso8601
    import aws_sdk_medialive.types.event_bridge_rule_template_event_type
    import aws_sdk_medialive.types.tag_map


class UpdateEventBridgeRuleTemplateResponse(TypedDict):
    arn: NotRequired[
        "aws_sdk_medialive.types.__string_pattern_arn_medialive_eventbridge_rule_template.__stringPatternArnMedialiveEventbridgeRuleTemplate"
    ]
    """An eventbridge rule template's ARN (Amazon Resource Name)"""
    created_at: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
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
    group_id: NotRequired[
        "aws_sdk_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """An eventbridge rule template group's id. AWS provided template groups have ids that start with `aws-`"""
    id: NotRequired[
        "aws_sdk_medialive.types.__string_min7_max11_pattern_aws097.__stringMin7Max11PatternAws097"
    ]
    """An eventbridge rule template's id. AWS provided templates have ids that start with `aws-`"""
    modified_at: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    name: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""
    tags: NotRequired["aws_sdk_medialive.types.tag_map.TagMap"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateEventBridgeRuleTemplateResponse) -> dict:
    out: dict = {}
    if "arn" in value:
        out["arn"] = value["arn"]
    if "created_at" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["createdAt"] = aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
            value["created_at"]
        )
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
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "id" in value:
        out["id"] = value["id"]
    if "modified_at" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["modifiedAt"] = aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
            value["modified_at"]
        )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> UpdateEventBridgeRuleTemplateResponse:
    out: UpdateEventBridgeRuleTemplateResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    if "createdAt" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["created_at"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["createdAt"]
            )
        )
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
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "id" in data:
        out["id"] = data["id"]
    if "modifiedAt" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["modified_at"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["modifiedAt"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.deserialize_json(data["tags"])
    return out
