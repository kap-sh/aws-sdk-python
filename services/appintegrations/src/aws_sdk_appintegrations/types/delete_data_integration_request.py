"""Generated from Smithy shape ``com.amazonaws.appintegrations#DeleteDataIntegrationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.identifier

class DeleteDataIntegrationRequest(TypedDict):
    data_integration_identifier: "aws_sdk_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataIntegrationRequest:
    out: DeleteDataIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out