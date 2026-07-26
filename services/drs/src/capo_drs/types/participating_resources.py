"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_drs.types.participating_resource

ParticipatingResources: TypeAlias = list[
    "capo_drs.types.participating_resource.ParticipatingResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingResources) -> list:
    import capo_drs.types.participating_resource

    out: list = []
    for item in value:
        out.append(capo_drs.types.participating_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipatingResources:
    import capo_drs.types.participating_resource

    out: ParticipatingResources = []
    for item in data:
        out.append(capo_drs.types.participating_resource.deserialize_json(item))
    return out
