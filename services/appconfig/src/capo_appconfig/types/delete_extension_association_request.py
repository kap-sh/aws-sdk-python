"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteExtensionAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appconfig.types.id


class DeleteExtensionAssociationRequest(TypedDict, closed=True):
    extension_association_id: "capo_appconfig.types.id.Id"
    """<p>The ID of the extension association to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExtensionAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExtensionAssociationRequest:
    out: DeleteExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
