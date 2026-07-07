"""Generated from Smithy shape ``com.amazonaws.supplychain#GetDataIntegrationEventRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.uuid


class GetDataIntegrationEventRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The Amazon Web Services Supply Chain instance identifier.</p>"""
    event_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The unique event identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataIntegrationEventRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataIntegrationEventRequest:
    out: GetDataIntegrationEventRequest = {}  # type: ignore[typeddict-item]
    return out
