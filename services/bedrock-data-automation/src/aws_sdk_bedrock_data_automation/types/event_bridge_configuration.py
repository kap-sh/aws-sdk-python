"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#EventBridgeConfiguration``."""

from typing import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError


class EventBridgeConfiguration(TypedDict):
    event_bridge_enabled: "bool"
    """Event bridge flag."""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeConfiguration) -> dict:
    out: dict = {}
    out["eventBridgeEnabled"] = value["event_bridge_enabled"]
    return out


def deserialize_json(data: dict) -> EventBridgeConfiguration:
    out: EventBridgeConfiguration = {}  # type: ignore[typeddict-item]
    if "eventBridgeEnabled" in data:
        out["event_bridge_enabled"] = data["eventBridgeEnabled"]
    else:
        raise DeserializationError(
            "EventBridgeConfiguration.event_bridge_enabled required"
        )
    return out
