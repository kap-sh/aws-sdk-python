"""Generated from Smithy shape ``com.amazonaws.datazone#DataZoneEntityType``."""

from typing import Literal, TypeAlias, cast

DataZoneEntityType: TypeAlias = Literal["DOMAIN_UNIT",]


# --- restJson1 ser/de ---
def serialize_json(value: DataZoneEntityType) -> str:
    return value


def deserialize_json(data: str) -> DataZoneEntityType:
    return cast(DataZoneEntityType, data)
