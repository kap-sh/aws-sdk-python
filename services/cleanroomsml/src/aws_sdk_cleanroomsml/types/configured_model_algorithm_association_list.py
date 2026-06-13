"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary

ConfiguredModelAlgorithmAssociationList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary.ConfiguredModelAlgorithmAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmAssociationList) -> list:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredModelAlgorithmAssociationList:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary

    out: ConfiguredModelAlgorithmAssociationList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.configured_model_algorithm_association_summary.deserialize_json(
                item
            )
        )
    return out
