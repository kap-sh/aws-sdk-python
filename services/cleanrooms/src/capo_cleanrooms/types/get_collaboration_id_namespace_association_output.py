"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationIdNamespaceAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_id_namespace_association


class GetCollaborationIdNamespaceAssociationOutput(TypedDict, closed=True):
    collaboration_id_namespace_association: "capo_cleanrooms.types.collaboration_id_namespace_association.CollaborationIdNamespaceAssociation"
    """<p>The ID namespace association that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationIdNamespaceAssociationOutput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_id_namespace_association

    out["collaborationIdNamespaceAssociation"] = (
        capo_cleanrooms.types.collaboration_id_namespace_association.serialize_json(
            value["collaboration_id_namespace_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationIdNamespaceAssociationOutput:
    out: GetCollaborationIdNamespaceAssociationOutput = {}  # type: ignore[typeddict-item]
    if "collaborationIdNamespaceAssociation" in data:
        import capo_cleanrooms.types.collaboration_id_namespace_association

        out["collaboration_id_namespace_association"] = (
            capo_cleanrooms.types.collaboration_id_namespace_association.deserialize_json(
                data["collaborationIdNamespaceAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationIdNamespaceAssociationOutput.collaboration_id_namespace_association required"
        )
    return out
