"""Generated from Smithy shape ``com.amazonaws.clouddirectory#FacetStyle``."""

from typing import Literal, TypeAlias, cast

FacetStyle: TypeAlias = Literal[
    "STATIC",
    "DYNAMIC",
]


# --- restJson1 ser/de ---
def serialize_json(value: FacetStyle) -> str:
    return value


def deserialize_json(data: str) -> FacetStyle:
    return cast(FacetStyle, data)
