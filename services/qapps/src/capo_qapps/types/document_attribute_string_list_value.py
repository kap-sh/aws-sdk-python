"""Generated from Smithy shape ``com.amazonaws.qapps#DocumentAttributeStringListValue``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qapps.types.plato_string

DocumentAttributeStringListValue: TypeAlias = list[
    "capo_qapps.types.plato_string.PlatoString"
]


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttributeStringListValue) -> list:
    return list(value)


def deserialize_json(data: list) -> DocumentAttributeStringListValue:
    return list(data)
