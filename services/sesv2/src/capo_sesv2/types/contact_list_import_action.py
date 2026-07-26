"""Generated from Smithy shape ``com.amazonaws.sesv2#ContactListImportAction``."""

from typing import Literal, TypeAlias, cast

ContactListImportAction: TypeAlias = Literal[
    "DELETE",
    "PUT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactListImportAction) -> str:
    return value


def deserialize_json(data: str) -> ContactListImportAction:
    return cast(ContactListImportAction, data)
