"""Generated from Smithy shape ``com.amazonaws.appintegrations#GetEventIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.name


class GetEventIntegrationRequest(TypedDict):
    name: "aws_sdk_appintegrations.types.name.Name"
    """<p>The name of the event integration. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventIntegrationRequest:
    out: GetEventIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
