"""Generated from Smithy shape ``com.amazonaws.qbusiness#DocumentAttributeStringListValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.string

DocumentAttributeStringListValue: TypeAlias = list["capo_qbusiness.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeStringListValue) -> list:
    return list(value)


def deserialize_json(data: list) -> DocumentAttributeStringListValue:
    return list(data)
