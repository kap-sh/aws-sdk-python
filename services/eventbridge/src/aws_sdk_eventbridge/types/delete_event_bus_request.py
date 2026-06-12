"""Generated from Smithy shape ``com.amazonaws.eventbridge#DeleteEventBusRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.event_bus_name


class DeleteEventBusRequest(TypedDict):
    name: "aws_sdk_eventbridge.types.event_bus_name.EventBusName"
    """<p>The name of the event bus to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventBusRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventBusRequest:
    out: DeleteEventBusRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DeleteEventBusRequest.name required")
    return out
