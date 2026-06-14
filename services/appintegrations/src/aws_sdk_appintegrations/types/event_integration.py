"""Generated from Smithy shape ``com.amazonaws.appintegrations#EventIntegration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn
    import aws_sdk_appintegrations.types.description
    import aws_sdk_appintegrations.types.event_bridge_bus
    import aws_sdk_appintegrations.types.event_filter
    import aws_sdk_appintegrations.types.name
    import aws_sdk_appintegrations.types.tag_map

class EventIntegration(TypedDict):
    event_integration_arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the event integration.</p>"""
    name: NotRequired["aws_sdk_appintegrations.types.name.Name"]
    """<p>The name of the event integration.</p>"""
    description: NotRequired["aws_sdk_appintegrations.types.description.Description"]
    """<p>The event integration description.</p>"""
    event_filter: NotRequired["aws_sdk_appintegrations.types.event_filter.EventFilter"]
    """<p>The event integration filter.</p>"""
    event_bridge_bus: NotRequired["aws_sdk_appintegrations.types.event_bridge_bus.EventBridgeBus"]
    """<p>The Amazon EventBridge bus for the event integration.</p>"""
    tags: NotRequired["aws_sdk_appintegrations.types.tag_map.TagMap"]
    """<p>The tags used to organize, track, or control access for this resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: EventIntegration) -> dict:
    out: dict = {}
    if "event_integration_arn" in value:
        out["EventIntegrationArn"] = value["event_integration_arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_filter" in value:
        import aws_sdk_appintegrations.types.event_filter
        out["EventFilter"] = aws_sdk_appintegrations.types.event_filter.serialize_json(value["event_filter"])
    if "event_bridge_bus" in value:
        out["EventBridgeBus"] = value["event_bridge_bus"]
    if "tags" in value:
        import aws_sdk_appintegrations.types.tag_map
        out["Tags"] = aws_sdk_appintegrations.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> EventIntegration:
    out: EventIntegration = {}  # type: ignore[typeddict-item]
    if "EventIntegrationArn" in data:
        out["event_integration_arn"] = data["EventIntegrationArn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventFilter" in data:
        import aws_sdk_appintegrations.types.event_filter
        out["event_filter"] = aws_sdk_appintegrations.types.event_filter.deserialize_json(data["EventFilter"])
    if "EventBridgeBus" in data:
        out["event_bridge_bus"] = data["EventBridgeBus"]
    if "Tags" in data:
        import aws_sdk_appintegrations.types.tag_map
        out["tags"] = aws_sdk_appintegrations.types.tag_map.deserialize_json(data["Tags"])
    return out