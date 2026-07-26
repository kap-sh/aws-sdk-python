"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ConfiguredAudienceModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_summary

ConfiguredAudienceModelList: TypeAlias = list[
    "capo_cleanroomsml.types.configured_audience_model_summary.ConfiguredAudienceModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfiguredAudienceModelList) -> list:
    import capo_cleanroomsml.types.configured_audience_model_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.configured_audience_model_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConfiguredAudienceModelList:
    import capo_cleanroomsml.types.configured_audience_model_summary

    out: ConfiguredAudienceModelList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.configured_audience_model_summary.deserialize_json(
                item
            )
        )
    return out
