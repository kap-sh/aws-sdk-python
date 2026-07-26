"""Generated from Smithy shape ``com.amazonaws.lambda#FullDocument``."""

from typing import Literal, TypeAlias, cast

FullDocument: TypeAlias = Literal[
    "UpdateLookup",
    "Default",
]


# --- restJson1 ser/de ---
def serialize_json(value: FullDocument) -> str:
    return value


def deserialize_json(data: str) -> FullDocument:
    return cast(FullDocument, data)
