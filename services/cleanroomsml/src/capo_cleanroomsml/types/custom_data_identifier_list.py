"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CustomDataIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.custom_data_identifier

CustomDataIdentifierList: TypeAlias = list[
    "capo_cleanroomsml.types.custom_data_identifier.CustomDataIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomDataIdentifierList) -> list:
    return list(value)


def deserialize_json(data: list) -> CustomDataIdentifierList:
    return list(data)
