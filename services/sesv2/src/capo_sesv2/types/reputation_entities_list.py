"""Generated from Smithy shape ``com.amazonaws.sesv2#ReputationEntitiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.reputation_entity

ReputationEntitiesList: TypeAlias = list[
    "capo_sesv2.types.reputation_entity.ReputationEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReputationEntitiesList) -> list:
    import capo_sesv2.types.reputation_entity

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.reputation_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReputationEntitiesList:
    import capo_sesv2.types.reputation_entity

    out: ReputationEntitiesList = []
    for item in data:
        out.append(capo_sesv2.types.reputation_entity.deserialize_json(item))
    return out
