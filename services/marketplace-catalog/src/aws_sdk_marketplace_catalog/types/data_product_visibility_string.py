"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#DataProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

DataProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Unavailable",
    "Draft",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> DataProductVisibilityString:
    return cast(DataProductVisibilityString, data)
