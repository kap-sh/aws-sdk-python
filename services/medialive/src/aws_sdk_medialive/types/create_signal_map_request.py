"""Generated from Smithy shape ``com.amazonaws.medialive#CreateSignalMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of__string_pattern_s
    import aws_sdk_medialive.types.__string_min0_max1024
    import aws_sdk_medialive.types.__string_min1_max255_pattern_s
    import aws_sdk_medialive.types.__string_min1_max256_pattern_s
    import aws_sdk_medialive.types.__string_min1_max2048
    import aws_sdk_medialive.types.tag_map


class CreateSignalMapRequest(TypedDict, closed=True):
    cloud_watch_alarm_template_group_identifiers: NotRequired[
        "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
    ]
    description: NotRequired[
        "aws_sdk_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    discovery_entry_point_arn: NotRequired[
        "aws_sdk_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A top-level supported AWS resource ARN to discovery a signal map from."""
    event_bridge_rule_template_group_identifiers: NotRequired[
        "aws_sdk_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
    ]
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
def serialize_json(value: CreateSignalMapRequest) -> dict:
    out: dict = {}
    if "cloud_watch_alarm_template_group_identifiers" in value:
        import aws_sdk_medialive.types.__list_of__string_pattern_s

        out["cloudWatchAlarmTemplateGroupIdentifiers"] = (
            aws_sdk_medialive.types.__list_of__string_pattern_s.serialize_json(
                value["cloud_watch_alarm_template_group_identifiers"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "discovery_entry_point_arn" in value:
        out["discoveryEntryPointArn"] = value["discovery_entry_point_arn"]
    if "event_bridge_rule_template_group_identifiers" in value:
        import aws_sdk_medialive.types.__list_of__string_pattern_s

        out["eventBridgeRuleTemplateGroupIdentifiers"] = (
            aws_sdk_medialive.types.__list_of__string_pattern_s.serialize_json(
                value["event_bridge_rule_template_group_identifiers"]
            )
        )
    if "name" in value:
        out["name"] = value["name"]
    if "tags" in value:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.serialize_json(value["tags"])
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    return out


def deserialize_json(data: dict) -> CreateSignalMapRequest:
    out: CreateSignalMapRequest = {}  # type: ignore[typeddict-item]
    if "cloudWatchAlarmTemplateGroupIdentifiers" in data:
        import aws_sdk_medialive.types.__list_of__string_pattern_s

        out["cloud_watch_alarm_template_group_identifiers"] = (
            aws_sdk_medialive.types.__list_of__string_pattern_s.deserialize_json(
                data["cloudWatchAlarmTemplateGroupIdentifiers"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "discoveryEntryPointArn" in data:
        out["discovery_entry_point_arn"] = data["discoveryEntryPointArn"]
    if "eventBridgeRuleTemplateGroupIdentifiers" in data:
        import aws_sdk_medialive.types.__list_of__string_pattern_s

        out["event_bridge_rule_template_group_identifiers"] = (
            aws_sdk_medialive.types.__list_of__string_pattern_s.deserialize_json(
                data["eventBridgeRuleTemplateGroupIdentifiers"]
            )
        )
    if "name" in data:
        out["name"] = data["name"]
    if "tags" in data:
        import aws_sdk_medialive.types.tag_map

        out["tags"] = aws_sdk_medialive.types.tag_map.deserialize_json(data["tags"])
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    return out
