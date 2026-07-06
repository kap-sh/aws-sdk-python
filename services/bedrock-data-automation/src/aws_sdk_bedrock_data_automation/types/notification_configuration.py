"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.event_bridge_configuration


class NotificationConfiguration(TypedDict, closed=True):
    event_bridge_configuration: "aws_sdk_bedrock_data_automation.types.event_bridge_configuration.EventBridgeConfiguration"
    """Event bridge configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.event_bridge_configuration

    out["eventBridgeConfiguration"] = (
        aws_sdk_bedrock_data_automation.types.event_bridge_configuration.serialize_json(
            value["event_bridge_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "eventBridgeConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.event_bridge_configuration

        out["event_bridge_configuration"] = (
            aws_sdk_bedrock_data_automation.types.event_bridge_configuration.deserialize_json(
                data["eventBridgeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationConfiguration.event_bridge_configuration required"
        )
    return out
