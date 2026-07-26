"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationConfiguredModelAlgorithmAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary

CollaborationConfiguredModelAlgorithmAssociationList: TypeAlias = list[
    "capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary.CollaborationConfiguredModelAlgorithmAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationConfiguredModelAlgorithmAssociationList) -> list:
    import capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> CollaborationConfiguredModelAlgorithmAssociationList:
    import capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary

    out: CollaborationConfiguredModelAlgorithmAssociationList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.collaboration_configured_model_algorithm_association_summary.deserialize_json(
                item
            )
        )
    return out
