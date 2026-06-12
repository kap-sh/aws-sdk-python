"""Generated from Smithy shape ``com.amazonaws.appconfig#GetExtensionAssociationRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.id


class GetExtensionAssociationRequest(TypedDict):
    extension_association_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The extension association ID to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExtensionAssociationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExtensionAssociationRequest:
    out: GetExtensionAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
