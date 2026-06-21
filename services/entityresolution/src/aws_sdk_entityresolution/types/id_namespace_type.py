"""Generated from Smithy shape ``com.amazonaws.entityresolution#IdNamespaceType``."""

from typing import Literal, TypeAlias, cast

IdNamespaceType: TypeAlias = Literal[
    "SOURCE",
    "TARGET",
]


# --- restJson1 ser/de ---
def serialize_json(value: IdNamespaceType) -> str:
    return value


def deserialize_json(data: str) -> IdNamespaceType:
    return cast(IdNamespaceType, data)
