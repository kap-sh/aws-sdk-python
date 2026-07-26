"""Generated from Smithy shape ``com.amazonaws.medialive#StartUpdateSignalMapRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__boolean
    import capo_medialive.types.__list_of__string_pattern_s
    import capo_medialive.types.__string
    import capo_medialive.types.__string_min0_max1024
    import capo_medialive.types.__string_min1_max255_pattern_s
    import capo_medialive.types.__string_min1_max2048


class StartUpdateSignalMapRequest(TypedDict, closed=True):
    cloud_watch_alarm_template_group_identifiers: NotRequired[
        "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
    ]
    description: NotRequired[
        "capo_medialive.types.__string_min0_max1024.__stringMin0Max1024"
    ]
    """A resource's optional description."""
    discovery_entry_point_arn: NotRequired[
        "capo_medialive.types.__string_min1_max2048.__stringMin1Max2048"
    ]
    """A top-level supported AWS resource ARN to discovery a signal map from."""
    event_bridge_rule_template_group_identifiers: NotRequired[
        "capo_medialive.types.__list_of__string_pattern_s.__listOf__stringPatternS"
    ]
    force_rediscovery: NotRequired["capo_medialive.types.__boolean.__boolean"]
    """If true, will force a rediscovery of a signal map if an unchanged discoveryEntryPointArn is provided."""
    identifier: "capo_medialive.types.__string.__string"
    """A signal map's identifier. Can be either be its id or current name."""
    name: NotRequired[
        "capo_medialive.types.__string_min1_max255_pattern_s.__stringMin1Max255PatternS"
    ]
    """A resource's name. Names must be unique within the scope of a resource type in a specific region."""


# --- restJson1 ser/de ---
def serialize_json(value: StartUpdateSignalMapRequest) -> dict:
    out: dict = {}
    if "cloud_watch_alarm_template_group_identifiers" in value:
        import capo_medialive.types.__list_of__string_pattern_s

        out["cloudWatchAlarmTemplateGroupIdentifiers"] = (
            capo_medialive.types.__list_of__string_pattern_s.serialize_json(
                value["cloud_watch_alarm_template_group_identifiers"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "discovery_entry_point_arn" in value:
        out["discoveryEntryPointArn"] = value["discovery_entry_point_arn"]
    if "event_bridge_rule_template_group_identifiers" in value:
        import capo_medialive.types.__list_of__string_pattern_s

        out["eventBridgeRuleTemplateGroupIdentifiers"] = (
            capo_medialive.types.__list_of__string_pattern_s.serialize_json(
                value["event_bridge_rule_template_group_identifiers"]
            )
        )
    if "force_rediscovery" in value:
        out["forceRediscovery"] = value["force_rediscovery"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> StartUpdateSignalMapRequest:
    out: StartUpdateSignalMapRequest = {}  # type: ignore[typeddict-item]
    if "cloudWatchAlarmTemplateGroupIdentifiers" in data:
        import capo_medialive.types.__list_of__string_pattern_s

        out["cloud_watch_alarm_template_group_identifiers"] = (
            capo_medialive.types.__list_of__string_pattern_s.deserialize_json(
                data["cloudWatchAlarmTemplateGroupIdentifiers"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "discoveryEntryPointArn" in data:
        out["discovery_entry_point_arn"] = data["discoveryEntryPointArn"]
    if "eventBridgeRuleTemplateGroupIdentifiers" in data:
        import capo_medialive.types.__list_of__string_pattern_s

        out["event_bridge_rule_template_group_identifiers"] = (
            capo_medialive.types.__list_of__string_pattern_s.deserialize_json(
                data["eventBridgeRuleTemplateGroupIdentifiers"]
            )
        )
    if "forceRediscovery" in data:
        out["force_rediscovery"] = data["forceRediscovery"]
    if "name" in data:
        out["name"] = data["name"]
    return out
