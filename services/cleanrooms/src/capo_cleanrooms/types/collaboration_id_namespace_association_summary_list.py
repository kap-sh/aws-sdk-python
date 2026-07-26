"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CollaborationIdNamespaceAssociationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary

CollaborationIdNamespaceAssociationSummaryList: TypeAlias = list[
    "capo_cleanrooms.types.collaboration_id_namespace_association_summary.CollaborationIdNamespaceAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationIdNamespaceAssociationSummaryList) -> list:
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanrooms.types.collaboration_id_namespace_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationIdNamespaceAssociationSummaryList:
    import capo_cleanrooms.types.collaboration_id_namespace_association_summary

    out: CollaborationIdNamespaceAssociationSummaryList = []
    for item in data:
        out.append(
            capo_cleanrooms.types.collaboration_id_namespace_association_summary.deserialize_json(
                item
            )
        )
    return out
