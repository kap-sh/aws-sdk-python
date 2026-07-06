"""Generated from Smithy shape ``com.amazonaws.supplychain#SendDataIntegrationEventResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_supplychain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.uuid


class SendDataIntegrationEventResponse(TypedDict, closed=True):
    event_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The unique event identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendDataIntegrationEventResponse) -> dict:
    out: dict = {}
    out["eventId"] = value["event_id"]
    return out


def deserialize_json(data: dict) -> SendDataIntegrationEventResponse:
    out: SendDataIntegrationEventResponse = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("SendDataIntegrationEventResponse.event_id required")
    return out
