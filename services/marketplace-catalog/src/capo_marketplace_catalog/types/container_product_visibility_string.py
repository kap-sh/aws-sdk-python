"""Generated from Smithy shape ``com.amazonaws.marketplacecatalog#ContainerProductVisibilityString``."""

from typing import Literal, TypeAlias, cast

ContainerProductVisibilityString: TypeAlias = Literal[
    "Limited",
    "Public",
    "Restricted",
    "Draft",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerProductVisibilityString) -> str:
    return value


def deserialize_json(data: str) -> ContainerProductVisibilityString:
    return cast(ContainerProductVisibilityString, data)
