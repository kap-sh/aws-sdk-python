"""Generated from Smithy shape ``com.amazonaws.efs#DestinationsToCreate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.destination_to_create

DestinationsToCreate: TypeAlias = list[
    "capo_efs.types.destination_to_create.DestinationToCreate"
]


# --- restJson1 ser/de ---
def serialize_json(value: DestinationsToCreate) -> list:
    import capo_efs.types.destination_to_create

    out: list = []
    for item in value:
        out.append(capo_efs.types.destination_to_create.serialize_json(item))
    return out


def deserialize_json(data: list) -> DestinationsToCreate:
    import capo_efs.types.destination_to_create

    out: DestinationsToCreate = []
    for item in data:
        out.append(capo_efs.types.destination_to_create.deserialize_json(item))
    return out
