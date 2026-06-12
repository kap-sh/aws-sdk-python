"""Generated from Smithy shape ``com.amazonaws.appsync#EventBridgeDataSourceConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_appsync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_appsync.types.string


class EventBridgeDataSourceConfig(TypedDict):
    event_bus_arn: "aws_sdk_appsync.types.string.String"
    """<p>The ARN of the event bus. For more information about event buses, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html\">Amazon EventBridge event buses</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EventBridgeDataSourceConfig) -> dict:
    out: dict = {}
    out["eventBusArn"] = value["event_bus_arn"]
    return out


def deserialize_json(data: dict) -> EventBridgeDataSourceConfig:
    out: EventBridgeDataSourceConfig = {}  # type: ignore[typeddict-item]
    if "eventBusArn" in data:
        out["event_bus_arn"] = data["eventBusArn"]
    else:
        raise DeserializationError("EventBridgeDataSourceConfig.event_bus_arn required")
    return out
