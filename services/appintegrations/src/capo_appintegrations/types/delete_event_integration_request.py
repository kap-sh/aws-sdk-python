"""Generated from Smithy shape ``com.amazonaws.appintegrations#DeleteEventIntegrationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appintegrations.types.name


class DeleteEventIntegrationRequest(TypedDict, closed=True):
    name: "capo_appintegrations.types.name.Name"
    """<p>The name of the event integration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventIntegrationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventIntegrationRequest:
    out: DeleteEventIntegrationRequest = {}  # type: ignore[typeddict-item]
    return out
