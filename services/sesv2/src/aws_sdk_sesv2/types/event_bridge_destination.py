"""Generated from Smithy shape ``com.amazonaws.sesv2#EventBridgeDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.amazon_resource_name


class EventBridgeDestination(TypedDict, closed=True):
    event_bus_arn: "aws_sdk_sesv2.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the Amazon EventBridge bus to publish email events to. Only the default bus is supported. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeDestination) -> dict:
    out: dict = {}
    out["EventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_json(data: dict) -> EventBridgeDestination:
    out: EventBridgeDestination = {}  # type: ignore[typeddict-item]
    if "EventBusArn" in data:
        out["event_bus_arn"] = data["EventBusArn"]
    else:
        raise DeserializationError("EventBridgeDestination.event_bus_arn required")
    return out
