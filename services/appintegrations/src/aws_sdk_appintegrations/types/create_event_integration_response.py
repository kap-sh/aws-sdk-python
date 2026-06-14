"""Generated from Smithy shape ``com.amazonaws.appintegrations#CreateEventIntegrationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.arn

class CreateEventIntegrationResponse(TypedDict):
    event_integration_arn: NotRequired["aws_sdk_appintegrations.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the event integration. </p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateEventIntegrationResponse) -> dict:
    out: dict = {}
    if "event_integration_arn" in value:
        out["EventIntegrationArn"] = value["event_integration_arn"]
    return out


def deserialize_json(data: dict) -> CreateEventIntegrationResponse:
    out: CreateEventIntegrationResponse = {}  # type: ignore[typeddict-item]
    if "EventIntegrationArn" in data:
        out["event_integration_arn"] = data["EventIntegrationArn"]
    return out