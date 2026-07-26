"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#NotificationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.event_bridge_configuration


class NotificationConfiguration(TypedDict, closed=True):
    event_bridge_configuration: "capo_bedrock_data_automation_runtime.types.event_bridge_configuration.EventBridgeConfiguration"
    """Event bridge configuration."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotificationConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation_runtime.types.event_bridge_configuration

    out["eventBridgeConfiguration"] = (
        capo_bedrock_data_automation_runtime.types.event_bridge_configuration.serialize_aws_json_1_1(
            value["event_bridge_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotificationConfiguration:
    out: NotificationConfiguration = {}  # type: ignore[typeddict-item]
    if "eventBridgeConfiguration" in data:
        import capo_bedrock_data_automation_runtime.types.event_bridge_configuration

        out["event_bridge_configuration"] = (
            capo_bedrock_data_automation_runtime.types.event_bridge_configuration.deserialize_aws_json_1_1(
                data["eventBridgeConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "NotificationConfiguration.event_bridge_configuration required"
        )
    return out
