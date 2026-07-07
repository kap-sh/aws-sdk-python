"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationIdNamespaceAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.collaboration_id_namespace_association


class GetCollaborationIdNamespaceAssociationOutput(TypedDict, closed=True):
    collaboration_id_namespace_association: "aws_sdk_cleanrooms.types.collaboration_id_namespace_association.CollaborationIdNamespaceAssociation"
    """<p>The ID namespace association that you requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCollaborationIdNamespaceAssociationOutput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.collaboration_id_namespace_association

    out["collaborationIdNamespaceAssociation"] = (
        aws_sdk_cleanrooms.types.collaboration_id_namespace_association.serialize_json(
            value["collaboration_id_namespace_association"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetCollaborationIdNamespaceAssociationOutput:
    out: GetCollaborationIdNamespaceAssociationOutput = {}  # type: ignore[typeddict-item]
    if "collaborationIdNamespaceAssociation" in data:
        import aws_sdk_cleanrooms.types.collaboration_id_namespace_association

        out["collaboration_id_namespace_association"] = (
            aws_sdk_cleanrooms.types.collaboration_id_namespace_association.deserialize_json(
                data["collaborationIdNamespaceAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationIdNamespaceAssociationOutput.collaboration_id_namespace_association required"
        )
    return out
