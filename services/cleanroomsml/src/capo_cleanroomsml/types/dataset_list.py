"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.dataset

DatasetList: TypeAlias = list["capo_cleanroomsml.types.dataset.Dataset"]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetList) -> list:
    import capo_cleanroomsml.types.dataset

    out: list = []
    for item in value:
        out.append(capo_cleanroomsml.types.dataset.serialize_json(item))
    return out


def deserialize_json(data: list) -> DatasetList:
    import capo_cleanroomsml.types.dataset

    out: DatasetList = []
    for item in data:
        out.append(capo_cleanroomsml.types.dataset.deserialize_json(item))
    return out
