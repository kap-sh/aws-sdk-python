"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DatasetType``."""

from typing import Literal, TypeAlias, cast

DatasetType: TypeAlias = Literal["INTERACTIONS",]


# --- restJson1 ser/de ---
def serialize_json(value: DatasetType) -> str:
    return value


def deserialize_json(data: str) -> DatasetType:
    return cast(DatasetType, data)
