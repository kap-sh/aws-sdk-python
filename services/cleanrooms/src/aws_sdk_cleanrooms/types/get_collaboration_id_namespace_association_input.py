"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationIdNamespaceAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_identifier
    import aws_sdk_cleanrooms.types.id_namespace_association_identifier


class GetCollaborationIdNamespaceAssociationInput(TypedDict, closed=True):
    collaboration_identifier: (
        "aws_sdk_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier of the collaboration that contains the ID namespace association that you want to retrieve.</p>"""
    id_namespace_association_identifier: "aws_sdk_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier"
    """<p>The unique identifier of the ID namespace association that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationIdNamespaceAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCollaborationIdNamespaceAssociationInput:
    out: GetCollaborationIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
    return out
