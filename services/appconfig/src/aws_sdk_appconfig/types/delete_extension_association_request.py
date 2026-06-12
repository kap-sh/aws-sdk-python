"""Generated from Smithy shape ``com.amazonaws.appconfig#DeleteExtensionAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id


class DeleteExtensionAssociationRequest(TypedDict):
    extension_association_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the extension association to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteExtensionAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteExtensionAssociationRequest:
    out: DeleteExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
