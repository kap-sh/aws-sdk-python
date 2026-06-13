"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ImageSourceBandList``."""

from typing import TypeAlias

ImageSourceBandList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ImageSourceBandList) -> list:
    return list(value)


def deserialize_json(data: list) -> ImageSourceBandList:
    return list(data)
