"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_model_summary

AudienceModelList: TypeAlias = list[
    "capo_cleanroomsml.types.audience_model_summary.AudienceModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceModelList) -> list:
    import capo_cleanroomsml.types.audience_model_summary

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.audience_model_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AudienceModelList:
    import capo_cleanroomsml.types.audience_model_summary

    out: AudienceModelList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.audience_model_summary.deserialize_json(item)
        )
    return out
