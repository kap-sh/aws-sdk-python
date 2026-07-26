"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmAssociationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn

ConfiguredModelAlgorithmAssociationArnList: TypeAlias = list[
    "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmAssociationArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConfiguredModelAlgorithmAssociationArnList:
    return list(data)
