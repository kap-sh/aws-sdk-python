"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListAssetPropertiesFilter``."""

from typing import Literal, TypeAlias, cast

ListAssetPropertiesFilter: TypeAlias = Literal[
    "ALL",
    "BASE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetPropertiesFilter) -> str:
    return value


def deserialize_json(data: str) -> ListAssetPropertiesFilter:
    return cast(ListAssetPropertiesFilter, data)
