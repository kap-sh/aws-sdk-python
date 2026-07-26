"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_summary

ConfiguredModelAlgorithmAssociationList: TypeAlias = list[
    "capo_cleanroomsml.types.configured_model_algorithm_association_summary.ConfiguredModelAlgorithmAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmAssociationList) -> list:
    import capo_cleanroomsml.types.configured_model_algorithm_association_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.configured_model_algorithm_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredModelAlgorithmAssociationList:
    import capo_cleanroomsml.types.configured_model_algorithm_association_summary

    out: ConfiguredModelAlgorithmAssociationList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.configured_model_algorithm_association_summary.deserialize_json(
                item
            )
        )
    return out
