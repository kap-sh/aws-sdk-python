"""Generated from Smithy shape ``com.amazonaws.datazone#DataProductItemType``."""

from typing import Literal, TypeAlias, cast

DataProductItemType: TypeAlias = Literal["ASSET",]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductItemType) -> str:
    return value


def deserialize_json(data: str) -> DataProductItemType:
    return cast(DataProductItemType, data)
