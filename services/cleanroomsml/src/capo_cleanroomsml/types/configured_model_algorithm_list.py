"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredModelAlgorithmList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_summary

ConfiguredModelAlgorithmList: TypeAlias = list[
    "capo_cleanroomsml.types.configured_model_algorithm_summary.ConfiguredModelAlgorithmSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredModelAlgorithmList) -> list:
    import capo_cleanroomsml.types.configured_model_algorithm_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.configured_model_algorithm_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredModelAlgorithmList:
    import capo_cleanroomsml.types.configured_model_algorithm_summary

    out: ConfiguredModelAlgorithmList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.configured_model_algorithm_summary.deserialize_json(
                item
            )
        )
    return out
