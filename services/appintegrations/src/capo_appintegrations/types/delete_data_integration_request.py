"""Generated from Smithy shape ``com.amazonaws.appintegrations#DeleteDataIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.identifier


class DeleteDataIntegrationRequest(TypedDict, closed=True):
    data_integration_identifier: "capo_appintegrations.types.identifier.Identifier"
    """<p>A unique identifier for the DataIntegration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataIntegrationRequest:
    out: DeleteDataIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
