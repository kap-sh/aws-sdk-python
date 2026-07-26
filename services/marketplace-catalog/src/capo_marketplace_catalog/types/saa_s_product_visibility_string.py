"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#SaaSProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

SaaSProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Draft",
]


# --- restJson1 ser/de ---
def serialize_json(value: SaaSProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> SaaSProductVisibilityString:
    return cast(SaaSProductVisibilityString, data)
