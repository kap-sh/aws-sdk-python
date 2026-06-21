"""Generated from Smithy shape ``com.amazonaws.quicksight#SheetContentType``."""

from typing import Literal, TypeAlias, cast

SheetContentType: TypeAlias = Literal[
    "PAGINATED",
    "INTERACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: SheetContentType) -> str:
    return value


def deserialize_json(data: str) -> SheetContentType:
    return cast(SheetContentType, data)
