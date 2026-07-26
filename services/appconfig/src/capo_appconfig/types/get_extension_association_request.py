"""Generated from Smithy shape ``com.amazonaws.appconfig#GetExtensionAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id


class GetExtensionAssociationRequest(TypedDict, closed=True):
    extension_association_id: "capo_appconfig.types.id.Id"
    """<p>The extension association ID to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExtensionAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExtensionAssociationRequest:
    out: GetExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
