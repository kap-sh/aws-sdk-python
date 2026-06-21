"""Generated from Smithy shape ``com.amazonaws.qapps#LibraryItemStatus``."""

from typing import Literal, TypeAlias, cast

LibraryItemStatus: TypeAlias = Literal[
    "PUBLISHED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: LibraryItemStatus) -> str:
    return value


def deserialize_json(data: str) -> LibraryItemStatus:
    return cast(LibraryItemStatus, data)
