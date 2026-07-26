"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteIdNamespaceAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.id_namespace_association_identifier
    import capo_cleanrooms.types.membership_identifier


class DeleteIdNamespaceAssociationInput(TypedDict, closed=True):
    id_namespace_association_identifier: "capo_cleanrooms.types.id_namespace_association_identifier.IdNamespaceAssociationIdentifier"
    """<p>The unique identifier of the ID namespace association that you want to delete.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID namespace association that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdNamespaceAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdNamespaceAssociationInput:
    out: DeleteIdNamespaceAssociationInput = {}  # type: ignore[typeddict-item]
    return out
