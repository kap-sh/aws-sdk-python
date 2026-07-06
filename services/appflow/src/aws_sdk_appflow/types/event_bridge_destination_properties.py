"""Generated from Smithy shape ``com.amazonaws.appflow#EventBridgeDestinationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appflow.types.error_handling_config
    import aws_sdk_appflow.types.object


class EventBridgeDestinationProperties(TypedDict, closed=True):
    object: "aws_sdk_appflow.types.object.Object"
    """<p> The object specified in the Amazon EventBridge flow destination. </p>"""
    error_handling_config: NotRequired[
        "aws_sdk_appflow.types.error_handling_config.ErrorHandlingConfig"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeDestinationProperties) -> dict:
    out: dict = {}
    out["object"] = value["object"]
    if "error_handling_config" in value:
        import aws_sdk_appflow.types.error_handling_config

        out["errorHandlingConfig"] = (
            aws_sdk_appflow.types.error_handling_config.serialize_json(
                value["error_handling_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> EventBridgeDestinationProperties:
    out: EventBridgeDestinationProperties = {}  # type: ignore[typeddict-item]
    if "object" in data:
        out["object"] = data["object"]
    else:
        raise DeserializationError("EventBridgeDestinationProperties.object required")
    if "errorHandlingConfig" in data:
        import aws_sdk_appflow.types.error_handling_config

        out["error_handling_config"] = (
            aws_sdk_appflow.types.error_handling_config.deserialize_json(
                data["errorHandlingConfig"]
            )
        )
    return out
